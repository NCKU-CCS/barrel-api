from .models import Bucket, BucketRecord, BucketStatistics, DengueBucket
from rest_framework import serializers


class BucketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bucket
        fields = '__all__'

class BucketRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BucketRecord
        fields = '__all__'

class BucketStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BucketStatistics
        fields = '__all__'

class DengueBucketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DengueBucket
        fields = '__all__'