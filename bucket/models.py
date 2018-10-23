from django.contrib.gis.db import models


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
    lng = models.FloatField()
    lat = models.FloatField()

    point = models.PointField(geography=True, srid=4326)
