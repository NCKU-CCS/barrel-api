from .models import Bucket, BucketRecord, BucketStatistics, DengueBucket
from rest_framework import serializers


class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = '__all__'

class BucketRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketRecord
        fields = '__all__'

class BucketStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketStatistics
        fields = '__all__'

class DengueBucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = DengueBucket
        fields = '__all__'