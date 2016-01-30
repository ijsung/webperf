# Upload stats files found in given directory, and upload them to localhost:8000

import csv
import json
import urllib2
import os
import sys
import argparse

class BenchmarkCtx:
  def __init__(self, date, tool, suite, benchmark):
    self.date = date
    self.tool = tool
    self.benchmark_suite = suite
    self.benchmark = benchmark


# Reads given stat file and return important numbers as a dict
def ReadStats(statfile):
  d = {
    'system.total_cycles': -1,
    'C0[0,0].inst_fetched':-1,
    'C0[0,0].inst_executed':-1,
    'C0[0,0].blocks_fetched':-1,
    'C0[0,0].blocks_committed':-1,
    'C0[0,0].blocks_flushed':-1,
    'C0[0,0].blocks_refreshed':-1
  }

  with open(statfile, 'rb') as csvfile:
    s = csv.reader(csvfile, delimiter=' ', skipinitialspace=True)
    for row in s:
      if d.has_key(row[0]):
        d[row[0]] = row[1]
    return d

# Parse one stat file and upload via POST
def UploadOneStat(statfile, ctx):
  benchmark = ctx.benchmark
  s = ReadStats(statfile)
  data = {
    'benchmark': benchmark,
    'speedup': 1.0,
    'rawcycles': s['system.total_cycles'],
    'insfetched': s['C0[0,0].inst_fetched'],
    'insexeced':  s['C0[0,0].inst_executed'],
    'blkfetched':   s['C0[0,0].blocks_fetched'],
    'blkexeced':    s['C0[0,0].blocks_committed'],
    'blkflushed':    s['C0[0,0].blocks_flushed'],
    'blkrefreshed':  s['C0[0,0].blocks_refreshed'],
  }
  if (ctx.date != ''):
    data['created'] = ctx.date

  req = urllib2.Request('http://localhost:8000/measurements/')
  req.add_header('Content-Type', 'application/json')
  respons = urllib2.urlopen(req, json.dumps(data))
  print "Finished uploading benchmark " + ctx.benchmark + " of " + ctx.benchmark_suite

# Create a new benchmark via POST
def CreateBenchmark(benchmark):
  data = {
    'benchmarkname': benchmark,
  }
  req = urllib2.Request('http://localhost:8000/benchmarks/')
  req.add_header('Content-Type', 'application/json')
  respons = urllib2.urlopen(req, json.dumps(data))

def UploadOrCreateOneBenchmark(statfile, ctx):
  try:
    UploadOneStat(statfile, ctx)
  except urllib2.HTTPError, e:
    if e.code == 400: # this happens if the benchmark is not created. Create it here.
      print "Creating benchmark: " + ctx.benchmark
      CreateBenchmark(ctx.benchmark)
      UploadOneStat(statfile, ctx)

# Assuming date\benchmark\*.stats
# Ignoring "date" for now - uses today's date instead
def FindStats(toplevel, tool, date):
  for dirname, dirnames, filenames in os.walk(toplevel):

  # Assuming the enclosing directory name is the benchmark name
    for filename in filenames:
      bench, ext = os.path.splitext(filename)
      if ext != ".stats":
        continue
      benchmark_suite = os.path.basename(dirname)
      ctx = BenchmarkCtx(date, 'LLVM', benchmark_suite, bench)
      UploadOrCreateOneBenchmark(os.path.join(dirname, filename), ctx)

desc = 'Upload emulator-generated stats files found in given directory, and upload them to localhost:8000. Caveats: forces today\'s date and ignores tool given'

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--dir', dest='directory', default='.',
                   help='the directory to scan (default: current directory)')
parser.add_argument('--tool', dest='tool', default='llvm',
                  help='the compiler tool used. (default: llvm) [FIXME currently ignored]')
parser.add_argument('--date', dest='created', default='',
                  help='the date of the measurment. muste be in MMMM-YY-DD format (default: today)')

args = parser.parse_args()
print "Searching " + args.directory

FindStats(args.directory, args.tool, args.created)


