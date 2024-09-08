from rest_framework import serializers
from .models import * 



class WishlistPackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistPackages
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):
    wishlistpackages = WishlistPackagesSerializer(many=True, read_only=True)
    class Meta:
        model = Wishlist
        fields = ['user', 'wishlistpackages']


