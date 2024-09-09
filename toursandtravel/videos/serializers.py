from rest_framework import serializers
from .models import HolidaysPackagesVideos



class HolidaysPackagesVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesVideos
        fields = ['id', 'video']
