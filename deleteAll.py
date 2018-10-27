import boto3
import json
import re
import twd97
import django

from io import BytesIO
from datetime import datetime, timedelta
from pprint import pprint
from openpyxl import load_workbook

import os

# My local environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dengue_report_api.settings")

django.setup()

from denguebucket.models import Bucket, BucketRecord, BucketStatistics, DengueBucket


# def generate_week_str(now_week_start, week_ago_num):
#     week_ago_start = now_week_start - timedelta(days=7 * week_ago_num)
#     week_ago_end = now_week_start - timedelta(days=1 * week_ago_num)
#     return '%s~%s' % (
#         week_ago_start.strftime("%Y-%m-%d"), week_ago_end.strftime("%Y-%m-%d"))

NO_DATA = -1

Bucket.objects.all().delete()
BucketRecord.objects.all().delete()
BucketStatistics.objects.all().delete()
