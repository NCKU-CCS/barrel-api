import uuid
from django.contrib.gis.db import models


class BucketRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # 流水號
    bucket_id = models.TextField()
    # 調查日期
    investigate_date = models.DateField()
    # 縣市、區、里
    county = models.TextField()
    town = models.TextField()
    village = models.TextField()
    # 卵數、埃及孵化卵數、白線孵化卵數
    egg_count = models.IntegerField(default=0)
    egypt_egg_count = models.IntegerField(default=0)
    white_egg_count = models.IntegerField(default=0)
    # 孑孓、埃及幼蟲、白線幼蟲
    larvae_count = models.IntegerField(default=0)
    egypt_larvae_count = models.IntegerField(default=0)
    white_larvae_count = models.IntegerField(default=0)
    note = models.TextField()
