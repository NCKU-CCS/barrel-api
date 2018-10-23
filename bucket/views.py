from django.shortcuts import render
from django.http import HttpResponse
from bucket.models import Bucket
import json


def index(request):
    if request.method != 'GET':
        return HttpResponse(status=400)
    buckets = Bucket.objects.all()
    bucket_dict = dict()
    for bucket in buckets:
        bucket_dict[bucket.id] = {
            'lng': bucket.lng,
            'lat': bucket.lat
        }
    return HttpResponse(json.dumps(bucket_dict), content_type="application/json")