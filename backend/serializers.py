from rest_framework import serializers
from backend.models import Benchmark, Measurement
#from django.contrib.auth.models import User

class BenchmarkSerializer(serializers.HyperlinkedModelSerializer):
  pass

class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
  benchmark = serializers.SlugRelatedField(
      many=False,
      slug_field='benchmarkname',
      queryset=Benchmark.objects.all()
      )
  class Meta:
    model = Measurement
    fields = ('id', 'created', 'benchmark', 'speedup',
              'rawcycles', 'insfetched', 'insexeced', 'blkfetched', 'blkexeced',
              'blkrefreshed', 'blkflushed')
                  
class BenchmarkSerializer(serializers.HyperlinkedModelSerializer):
  measurements = MeasurementSerializer(many=True, read_only=True)
  class Meta:
    model = Benchmark
    fields = ('benchmarkname', 'measurements')
    extra_kwargs = {
      'url': {'view_name':'benchmarks', 'lookup_field': 'benchmarkname' }
    }

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    measurements = serializers.HyperlinkedRelatedField(queryset=Measurement.objects.all(), view_name='measurement-detail', many=True)
#
#    class Meta:
#        model = User
#        fields = ('url', 'username', 'measurements')
