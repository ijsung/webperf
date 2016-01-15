from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import BenchmarkSerializer

class CreateBenchmarkTest(APITestCase):
    def setUp(self):
      self.data =  {'benchmarkname' : 'Parboil_BFS'}
    def test_can_create_benchmark(self):
      response = self.client.post(reverse('benchmark-list'), self.data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CreateMeasurementTest(APITestCase):
    def setUp(self):
      self.data =  {'benchmarkname' : 'test2'}
    def test_can_create_benchmark(self):
      response = self.client.post(reverse('benchmark-list'), self.data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      response = self.client.post(reverse('measurement-list'),
          {
          'created' : '2015-1-3',
          'benchmark' : 'test2',
          'speedup' : 1.3
          }
          , format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
