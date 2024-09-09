from rest_framework import serializers
from .models import HolidaysPackagesGallery

class HolidaysPackagesGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesGallery
        fields = ['id', 'image']
        ref_name = 'HolidaysPackagesGallery'