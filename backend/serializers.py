from rest_framework import serializers
from backend.models import Benchmark, Measurement
#from django.contrib.auth.models import User
from taggit_serializer.serializers import(
  TagListSerializerField,
  TaggitSerializer)

class BenchmarkSerializer(serializers.HyperlinkedModelSerializer):
  pass

class MeasurementSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
  benchmark = serializers.SlugRelatedField(
      many=False,
      slug_field='benchmarkname',
      queryset=Benchmark.objects.all()
      )
  tags = TagListSerializerField()

  class Meta:
    model = Measurement
    fields = ('id', 'created', 'benchmark', 'speedup',
              'rawcycles', 'insfetched', 'insexeced', 'blkfetched', 'blkexeced',
              'blkrefreshed', 'blkflushed', 'tags')
                  
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
