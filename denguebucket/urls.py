from django.conf.urls import url
from rest_framework import routers
from .views import BucketViewSet, BucketRecordViewSet, BucketStatisticsViewSet, DengueBucketViewSet

router = routers.DefaultRouter()
router.register(r'bucket', BucketViewSet, 'Bucket')
router.register(r'bucket-record', BucketRecordViewSet, 'BucketRecord')
router.register(r'bucket-statistics', BucketStatisticsViewSet, 'BucketStatistics')
router.register(r'dengue-bucket', DengueBucketViewSet, 'DengueBucket')

urlpatterns = router.urls