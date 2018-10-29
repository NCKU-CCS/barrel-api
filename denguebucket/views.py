from django.shortcuts import render

# Create your views here.

from .models import Bucket, BucketRecord, BucketStatistics, DengueBucket
from .serializers import BucketSerializer, BucketRecordSerializer, BucketStatisticsSerializer, DengueBucketSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response 

from rest_framework.decorators import action, list_route, detail_route


import twd97
import json
from datetime import datetime, timedelta
from django.http import HttpResponse
class BucketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = BucketSerializer
    queryset = Bucket.objects.all()

    def list(self, request, *args, **kwargs):
        buckets = Bucket.objects.all()
        bucket_dict = dict()
        for bucket in buckets:
            bucket_dict[bucket.id] = {
                'lng': bucket.lng,
                'lat': bucket.lat
            }
        return HttpResponse(json.dumps(bucket_dict), content_type="application/json")

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
