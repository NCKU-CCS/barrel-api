from django.contrib import admin

# Register your models here.

from .models import DengueBucket, Bucket, BucketRecord, BucketStatistics

admin.site.register(Bucket)
admin.site.register(BucketRecord)
admin.site.register(BucketStatistics)
admin.site.register(DengueBucket)
