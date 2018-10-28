from django.contrib.gis.db import models
import uuid
# Create your models here.

class DengueBucket(models.Model):
    # 流水號
    id = models.TextField(primary_key=True)
    # 座標WS84 X, Y
    ws84_x = models.FloatField()
    ws84_y = models.FloatField()
    # 地址
    address = models.TextField()
    # 備註
    note = models.TextField()
    # WS84轉換成經緯度座標
    lng = models.FloatField()
    lat = models.FloatField()

    point = models.PointField(geography=True, srid=4326)

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

class Bucket(models.Model):
    # 流水號
    id = models.TextField(primary_key=True)
    # 座標WS84 X, Y
    ws84_x = models.FloatField()
    ws84_y = models.FloatField()
    # 地址
    address = models.TextField()
    # 備註
    note = models.TextField()
    # WS84轉換成經緯度座標
    lng = models.FloatField(default=0)
    lat = models.FloatField(default=0)

    point = models.PointField(geography=True, srid=4326, default=0)

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

class BucketStatistics(models.Model):
    # 調查日期
    investigate_date = models.DateField()
    # 縣市、區、里
    county = models.TextField()
    town = models.TextField()
    village = models.TextField()
    # 統計卵數
    total_egg_count = models.IntegerField(default=0)
    # 陽性率
    positive_rate = models.FloatField(default=0)
    # 平均卵數（十桶）
    avg_egg_count = models.FloatField(default=0)