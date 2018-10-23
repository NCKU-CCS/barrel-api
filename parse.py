
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

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dengue_report_api.settings")
django.setup()

from bucket.models import Bucket
from bucketRecord.models import BucketRecord
from bucketStatistics.models import BucketStatistics



Bucket(id='112',
    ws84_x=12.0,
    ws84_y=12.0,
    address='12133',
    note='1233',
    lng=12.0,
    lat=12.0,
    point='POINT(%f %f)' % (12.0, 12.0),
    ).save()