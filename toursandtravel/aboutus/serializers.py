from rest_framework import serializers
from .models import AboutUs, AboutVisa, VisaPoints, Homescreen


class HomescreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homescreen
        fields = '__all__'



class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'



from rest_framework import serializers
from .models import AboutUs, AboutVisa, VisaPoints

class VisaPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaPoints
        fields = ['id', 'point', 'about_visa']

class AboutVisaSerializer(serializers.ModelSerializer):
    visa_points = VisaPointsSerializer(many=True, read_only=True)

    class Meta:
        model = AboutVisa
        fields = ['id', 'logo', 'title', 'about', 'visa_points']

class AboutUsdetailSerializer(serializers.ModelSerializer):
    about_visa = AboutVisaSerializer(many=True, read_only=True)

    class Meta:
        model = AboutUs
        fields = ['id', 'slug', 'title', 'description', 'image1', 'image2', 'about_visa']