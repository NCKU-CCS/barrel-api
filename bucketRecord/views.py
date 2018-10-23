from django.shortcuts import render
from django.http import HttpResponse
from bucketRecord.models import BucketRecord
from datetime import datetime, timedelta
import json


def index(request):
    if request.method != 'GET':
        return HttpResponse(status=400)
    
    start = request.GET.get('start')
    if not start:
        start = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    end = request.GET.get('end')
    if not end:
        end = datetime.now().strftime("%Y-%m-%d")
    county = request.GET.get('county')
    if not county:
        county = '台南'
    try:
        bucketRecords = BucketRecord.objects.filter(
            investigate_date__lte=end
            ).filter(
            investigate_date__gte=start
            ).filter(county=county)
    except:
        return HttpResponse(status=400)

    town = request.GET.get('town')
    village = request.GET.get('village')

    if town:
        bucketRecords = bucketRecords.filter(town=town)
        if village:
            bucketRecords = bucketRecords.filter(village=village)

    res = dict()
    res['bucket-record'] = []
    for item in bucketRecords:
        record = {
            "investigate_date": item.investigate_date.strftime("%Y-%m-%d"),
            "bucket_id": item.bucket_id,
            "county": item.county,
            "town": item.town,
            "village": item.village,
            "egg_count": item.egg_count,
            "egypt_egg_count": item.egypt_egg_count,
            "white_egg_count": item.white_egg_count,
            "larvae_count": item.larvae_count,
            "egypt_larvae_count": item.egypt_larvae_count,
            "white_larvae_count": item.white_larvae_count,
            "note": item.note
        }
        res['bucket-record'].append(record)

    return HttpResponse(json.dumps(res), content_type="application/json")
