from __future__ import unicode_literals

from django.db import models
from datetime import date

# One performance measurement
class Measurement(models.Model):
    created = models.DateField(default=date.today)
    suite = models.CharField(max_length=30)
    benchmark = models.CharField(max_length=50)
    speedup = models.FloatField()
#    owner = models.ForeignKey('auth.User', related_name='measurements')

    class Meta:
        ordering = ('created',)

