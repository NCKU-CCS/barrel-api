from django.shortcuts import render

# Create your views here.

from .models import Bucket, BucketRecord, BucketStatistics, DengueBucket
from .serializers import BucketSerializer, BucketRecordSerializer, BucketStatisticsSerializer, DengueBucketSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response 
from rest_framework.decorators import action
from django.http import HttpResponse

import twd97
import json
from datetime import datetime, timedelta

class BucketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = BucketSerializer
    queryset = Bucket.objects.all()

    @action(detail=False, methods=['get'])
    def set_password(self, request, pk=None):
        print ("testing")
        return HttpResponse(json.dumps(dict()), content_type="application/json")

    @action(detail=False, methods=['get'])
    def location(self, request, *args, **kwargs):
        buckets = Bucket.objects.all()
        bucket_dict = dict()
        for bucket in buckets:
            bucket_dict[bucket.id] = {
                'lng': bucket.lng,
                'lat': bucket.lat
            }
        return HttpResponse(json.dumps(bucket_dict), content_type="application/json")

    def update(self, request, *args, **kwargs):
        bucket = self.get_object()
        serializer = BucketSerializer(bucket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class BucketRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BucketRecord.objects.all()
    serializer_class = BucketRecordSerializer

    def get_queryset(self):
        hasParams = bool(self.request.query_params)
        if hasParams is False:
            queryset = BucketRecord.objects.all()
            return queryset
        else:
            start = self.request.query_params.get('start')
            print (start)
            if start is None:
                start = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            end = self.request.query_params.get('end')
            print (end)
            if end is None:
                end = datetime.now().strftime("%Y-%m-%d")
            county = self.request.query_params.get('county')
            print (county)
            if county is None:
                county = '台南'
            try:
                queryset = BucketRecord.objects.filter(
                    investigate_date__lte=end
                    ).filter(
                    investigate_date__gte=start
                    ).filter(county=county)
            except:
                return HttpResponse(status=400)

            town = self.request.query_params.get('town')
            print (town)
            village = self.request.query_params.get('village')
            print (village)

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
