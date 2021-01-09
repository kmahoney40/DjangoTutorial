from rest_framework import serializers
from .models import Bucketlist
from water.models import Temp, RunTimes

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class TempSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Temp
        fields = ('id', 't1', 't2', 't3', 't4', 't5', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class RunTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunTimes
        fields = ('id', 'day', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7')
        read_only_fields = ('date_created', 'date_modified')
