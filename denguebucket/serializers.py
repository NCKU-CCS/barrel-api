from .models import Bucket, BucketRecord, BucketStatistics, DengueBucket
from rest_framework import serializers

import twd97

class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = '__all__'
        # fields = ('id', 'ws84_x', 'ws84_y', 'address', 'note')

    def create(self, validated_data):
        bucket_id = validated_data.get('id')
        ws84_x = validated_data.get('ws84_x')
        ws84_y = validated_data.get('ws84_y')
        address = validated_data.get('address')
        note = validated_data.get('note')
        bucket_lat, bucket_lng = twd97.towgs84(float(ws84_x), float(ws84_y))
        return Bucket.objects.create(
            id = bucket_id,
            ws84_x = ws84_x,
            ws84_y = ws84_y,
            address = address,
            note = note,
            lng = float(bucket_lng),
            lat = float(bucket_lat),
            point='POINT(%f %f)' % (ws84_x, ws84_y)
        )

    def update(self, instance, validated_data):
        instance.ws84_x = validated_data.get('ws84_x', instance.ws84_x)
        instance.ws84_y = validated_data.get('ws84_y', instance.ws84_y)
        instance.address = validated_data.get('address', instance.address)
        instance.note = validated_data.get('note', instance.note)
        bucket_lat, bucket_lng = twd97.towgs84(float(instance.ws84_x), float(instance.ws84_y))
        instance.lng = bucket_lng
        instance.lat = bucket_lat
        instance.point = 'POINT(%f %f)' % (float(instance.ws84_x), float(instance.ws84_y))
        instance.save()
        return instance

class BucketRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketRecord
        # fields = '__all__'
        exclude = ('id',)

class BucketStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketStatistics
        fields = '__all__'

class DengueBucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = DengueBucket
        fields = '__all__'