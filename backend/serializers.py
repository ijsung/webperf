from rest_framework import serializers
from backend.models import Measurement
#from django.contrib.auth.models import User


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
#    owner = serializers.ReadOnlyField(source='owner.username')
#highlight = serializers.HyperlinkedIdentityField(view_name='measurements-highlight', format='html')

    class Meta:
        model = Measurement
        fields = ('created', 'suite', 'benchmark', 'speedup')
                  
#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    measurements = serializers.HyperlinkedRelatedField(queryset=Measurement.objects.all(), view_name='measurement-detail', many=True)
#
#    class Meta:
#        model = User
#        fields = ('url', 'username', 'measurements')
