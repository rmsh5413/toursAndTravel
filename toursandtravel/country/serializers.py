

from rest_framework import serializers
from .models import *



class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['id', 'name', 'ordering', 'slug', 'image']
        ref_name = 'Cities'


class CountriesSerializer(serializers.ModelSerializer):
    cities = CitiesSerializer(many=True, read_only=True)

    class Meta:
        model = Countries
        fields = ['id', 'continent', 'name', 'ordering', 'slug', 'image', 'cities']
        ref_name = 'Countries'

    def create(self, validated_data):
        cities_data = validated_data.pop('cities', [])
        country = Countries.objects.create(**validated_data)

        for city_data in cities_data:
            Cities.objects.create(country=country, **city_data)

        return country


