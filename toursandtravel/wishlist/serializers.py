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
        fields = '__all__'
        
    def create(self, validated_data):
        wishlistpackages_data = validated_data.pop('wishlistpackages')
        wishlist = Wishlist.objects.create(**validated_data)
        for wishlistpackage_data in wishlistpackages_data:
            WishlistPackages.objects.create(wishlist=wishlist, **wishlistpackage_data)
        return wishlist

    def update(self, instance, validated_data):
        wishlistpackages_data = validated_data.pop('wishlistpackages')
        wishlistpackages = (instance.wishlistpackages).all()
        wishlistpackages = list(wishlistpackages)
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        for wishlistpackage_data in wishlistpackages_data:
            wishlistpackage = wishlistpackages.pop(0)
            wishlistpackage.package = wishlistpackage_data.get('package', wishlistpackage.package)
            wishlistpackage.save()
        return instance