from rest_framework import serializers
from .models import HolidaysPackagesType, HolidaysPackagesCategory

class HolidaysPackagesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesCategory
        fields = ['id', 'name', 'ordering', 'slug', 'image']

class HolidaysPackagesTypeSerializer(serializers.ModelSerializer):
    categories = HolidaysPackagesCategorySerializer(many=True, read_only=True)

    class Meta:
        model = HolidaysPackagesType
        fields = ['id', 'name', 'ordering', 'slug', 'image', 'categories']



