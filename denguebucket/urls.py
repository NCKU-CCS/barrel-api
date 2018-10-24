from django.conf.urls import url
from rest_framework import routers
from .views import BucketViewSet, BucketRecordViewSet, BucketStatisticsViewSet, DengueBucketViewSet

router = routers.DefaultRouter()
router.register(r'bucket', BucketViewSet)
router.register(r'bucket-record', BucketRecordViewSet)
router.register(r'bucket-statistics', BucketStatisticsViewSet)
router.register(r'dengue-bucket', DengueBucketViewSet)

urlpatterns = router.urls