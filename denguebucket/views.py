from django.shortcuts import render

# Create your views here.

from .models import Bucket, BucketRecord, BucketStatistics, DengueBucket
from .serializers import BucketSerializer, BucketRecordSerializer, BucketStatisticsSerializer, DengueBucketSerializer
from rest_framework import viewsets
from rest_framework.response import Response 

import twd97
from datetime import datetime, timedelta
class BucketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = BucketSerializer
    queryset = Bucket.objects.all()

class BucketRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BucketRecord.objects.all()
    serializer_class = BucketRecordSerializer

class BucketStatisticsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BucketStatistics.objects.all()
    serializer_class = BucketStatisticsSerializer

class DengueBucketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DengueBucket.objects.all()
    serializer_class = DengueBucketSerializer
