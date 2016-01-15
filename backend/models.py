from __future__ import unicode_literals

from django.db import models
from datetime import date

# One benchmark suite
class BenchmarkSuite(models.Model):
  name = models.CharField(max_length=50)

# One benchmark
class Benchmark(models.Model):
  benchmarkname = models.CharField(max_length=50, unique=True)
#  suite = models.ForeignKey(BenchmarkSuite)
  class Meta:
    ordering = ('benchmarkname',)


# One performance measurement
class Measurement(models.Model):
  created = models.DateField(default=date.today)
  benchmark = models.ForeignKey(Benchmark, related_name='measurements')
  speedup = models.FloatField()
#    owner = models.ForeignKey('auth.User', related_name='measurements')

  class Meta:
    ordering = ('created',)

