from rest_framework import serializers
from .models import *


class HolidaysPackagesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesCategory
        fields = '__all__'


class HolidaysPackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackages
        fields = '__all__'