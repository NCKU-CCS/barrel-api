from django.contrib.gis.db import models

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