from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from backend.models import Measurement
from backend.permissions import IsOwnerOrReadOnly
from backend.serializers import MeasurementSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents benchmark measurements 
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

