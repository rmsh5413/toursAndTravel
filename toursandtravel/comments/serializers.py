from rest_framework import serializers
from .models import HolidaysPackagesComments



class HolidaysPackagesCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesComments
        fields = ['id', 'comment' ]  
