from django.shortcuts import render

# Create your views here.

from .models import Bucket, BucketRecord, BucketStatistics, DengueBucket
from .serializers import BucketSerializer, BucketRecordSerializer, BucketStatisticsSerializer, DengueBucketSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response 
from rest_framework.decorators import action, api_view
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from django.http import HttpResponse
from django.core.cache import cache

import twd97
import json
from datetime import datetime, timedelta

class BucketViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = BucketSerializer
    queryset = Bucket.objects.all()

    @action(methods = ['get'], detail = False)
    def location(self, request, *args, **kwargs):
        buckets = Bucket.objects.all()
        bucket_dict = dict()
        for bucket in buckets:
            bucket_dict[bucket.id] = {
                'lng': bucket.lng,
                'lat': bucket.lat
            }
        return Response(bucket_dict)    

    def put(self, request, *args, **kwargs):
        bucket = self.get_object()
        serializer = BucketSerializer(bucket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def create(self, request):
        bucket = self.get_object()
        serializer = BucketSerializer(bucket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def destroy(self, request, pk):
        Bucket.objects.delete(id = pk)
        


class BucketRecordViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = BucketRecord.objects.all()
    serializer_class = BucketRecordSerializer

    def get_queryset(self):
        hasParams = bool(self.request.query_params)
        if hasParams is False:
            queryset = BucketRecord.objects.all()
            return queryset
        else:
            start = self.request.query_params.get('start')
            if start is None:
                start = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            end = self.request.query_params.get('end')
            if end is None:
                end = datetime.now().strftime("%Y-%m-%d")
            county = self.request.query_params.get('county')
            if county is None:
                county = '台南'
            try:
                queryset = BucketRecord.objects.filter(
                    investigate_date__lte=end
                    ).filter(
                    investigate_date__gte=start
                    ).filter(county=county)
            except:
                return Response(status=400)

            town = self.request.query_params.get('town')
            village = self.request.query_params.get('village')

            if town is not None:
                queryset = queryset.filter(town=town)
                if village is not None:
                    queryset = queryset.filter(village=village)
            
            return queryset

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
