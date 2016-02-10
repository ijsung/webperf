from __future__ import unicode_literals

from django.db import models
from datetime import date
from taggit.managers import TaggableManager

# One benchmark suite
class BenchmarkSuite(models.Model):
  name = models.CharField(max_length=50)

# One benchmark
class Benchmark(models.Model):
  benchmarkname = models.CharField(max_length=50, unique=True, help_text="Please use BenchmarkSuite_Benchmark format")
#  suite = models.ForeignKey(BenchmarkSuite)
  class Meta:
    ordering = ('benchmarkname',)


# One performance measurement
class Measurement(models.Model):
  created = models.DateField(default=date.today, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
  benchmark = models.ForeignKey(Benchmark, related_name='measurements', help_text="Please use an existing benchmark name")
  speedup = models.FloatField()
  rawcycles = models.BigIntegerField(help_text="Raw Cycles", default="-1")
  insfetched = models.BigIntegerField(help_text="Instruction fetched", default="-1")
  insexeced = models.BigIntegerField(help_text="Instruction executed", default="-1")
  blkfetched = models.BigIntegerField(help_text="Blocks fetched", default="-1")
  blkexeced = models.BigIntegerField(help_text="Blocks executed", default="-1")
  blkrefreshed = models.BigIntegerField(help_text="Blocks refreshed", default="-1")
  blkflushed = models.BigIntegerField(help_text="Blocks flushed", default="-1")
  tags = TaggableManager(blank=True)

#    owner = models.ForeignKey('auth.User', related_name='measurements')

  class Meta:
    ordering = ('created',)

