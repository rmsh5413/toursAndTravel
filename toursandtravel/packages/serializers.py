from rest_framework import serializers
from .models import *
from gallery.models import *
from videos.models import *
from comments.models import HolidaysPackagesComments
from rest_framework import generics
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from datetime import datetime



class HolidaysPackagesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesCategory
        fields = '__all__'


class HolidaysPackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackages
        fields = '__all__'


from rest_framework import serializers

class HolidaysPackagesFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesFaq
        fields = ['id', 'ordering', 'question', 'answer']

class HolidaysPackagesHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesHighlights
        fields = ['id', 'ordering', 'detail']

class HolidaysPackagesGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesGallery
        fields = ['id', 'image']

class HolidaysPackagesVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesVideos
        fields = ['id', 'video']

class HolidaysPackagesInclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesInclusion
        fields = ['id', 'ordering', 'detail']

class HolidaysPackagesExclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesExclusion
        fields = ['id', 'ordering', 'detail']

class HolidaysPackagesNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesNotice
        fields = ['id', 'ordering', 'title', 'description']

class HolidaysPackagesDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesDates
        fields = ['id', 'start_date', 'end_date']


class HolidaysPackagesFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesFaq
        fields = ['id', 'ordering', 'question', 'answer']


class HolidaysPackagesCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesComments
        fields = ['id', 'comment' ]  


class HolidaysPackagesHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesHighlights
        fields = ['id', 'ordering', 'detail']

class HolidaysPackagesSerializer(serializers.ModelSerializer):
    faqs = HolidaysPackagesFaqSerializer(many=True, required=False)
    highlights = HolidaysPackagesHighlightsSerializer(many=True, required=False)
    gallery = HolidaysPackagesGallerySerializer(many=True, required=False)
    videos = HolidaysPackagesVideosSerializer(many=True, required=False)
    inclusions = HolidaysPackagesInclusionSerializer(many=True, required=False)
    exclusions = HolidaysPackagesExclusionSerializer(many=True, required=False)
    notices = HolidaysPackagesNoticeSerializer(many=True, required=False)
    dates = HolidaysPackagesDatesSerializer(many=True, required=False)

    class Meta:
        model = HolidaysPackages
        fields = [
            'id','country','city', 'packagetype', 'category', 'ordering', 'name', 'slug', 'description',
            'image', 'price', 'destination', 'duration', 'start_point', 'end_point',
            'group_size', 'season', 'meals', 'select_package_type', 'accommodations',
            'activity_duration', 'max_altitude', 'youtubeUrl', 'mapUrl', 'pdfManual',
            'faqs', 'highlights', 'gallery', 'videos', 'inclusions', 'exclusions',
            'notices', 'dates'
        ]

    def create(self, validated_data):
        faqs_data = validated_data.pop('faqs', [])
        highlights_data = validated_data.pop('highlights', [])
        gallery_data = validated_data.pop('gallery', [])
        videos_data = validated_data.pop('videos', [])
        inclusions_data = validated_data.pop('inclusions', [])
        exclusions_data = validated_data.pop('exclusions', [])
        notices_data = validated_data.pop('notices', [])
        dates_data = validated_data.pop('dates', [])

        holiday_package = HolidaysPackages.objects.create(**validated_data)

        for faq_data in faqs_data:
            HolidaysPackagesFaq.objects.create(package=holiday_package, **faq_data)
        for highlight_data in highlights_data:
            HolidaysPackagesHighlights.objects.create(package=holiday_package, **highlight_data)
        for gallery_item_data in gallery_data:
            HolidaysPackagesGallery.objects.create(package=holiday_package, **gallery_item_data)
        for video_data in videos_data:
            HolidaysPackagesVideos.objects.create(package=holiday_package, **video_data)
        for inclusion_data in inclusions_data:
            HolidaysPackagesInclusion.objects.create(package=holiday_package, **inclusion_data)
        for exclusion_data in exclusions_data:
            HolidaysPackagesExclusion.objects.create(package=holiday_package, **exclusion_data)
        for notice_data in notices_data:
            HolidaysPackagesNotice.objects.create(package=holiday_package, **notice_data)
        for date_data in dates_data:
            HolidaysPackagesDates.objects.create(package=holiday_package, **date_data)

        return holiday_package


class UpdateHolidaysPackagesSerializer(serializers.ModelSerializer):
    faqs = HolidaysPackagesFaqSerializer(many=True, required=False)
    highlights = HolidaysPackagesHighlightsSerializer(many=True, required=False)
    gallery = HolidaysPackagesGallerySerializer(many=True, required=False)
    videos = HolidaysPackagesVideosSerializer(many=True, required=False)
    inclusions = HolidaysPackagesInclusionSerializer(many=True, required=False)
    exclusions = HolidaysPackagesExclusionSerializer(many=True, required=False)
    notices = HolidaysPackagesNoticeSerializer(many=True, required=False)
    dates = HolidaysPackagesDatesSerializer(many=True, required=False)

    class Meta:
        model = HolidaysPackages
        fields = [
            'id', 'country', 'city', 'packagetype', 'category', 'ordering', 'name', 'slug', 'description',
            'image', 'price', 'destination', 'duration', 'start_point', 'end_point',
            'group_size', 'season', 'meals', 'select_package_type', 'accommodations',
            'activity_duration', 'max_altitude', 'youtubeUrl', 'mapUrl', 'pdfManual',
            'faqs', 'highlights', 'gallery', 'videos', 'inclusions', 'exclusions', 'notices', 'dates'
        ]

    def update(self, instance, validated_data):
        # Update HolidaysPackages fields
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.start_point = validated_data.get('start_point', instance.start_point)
        instance.end_point = validated_data.get('end_point', instance.end_point)
        instance.group_size = validated_data.get('group_size', instance.group_size)
        instance.season = validated_data.get('season', instance.season)
        instance.meals = validated_data.get('meals', instance.meals)
        instance.select_package_type = validated_data.get('select_package_type', instance.select_package_type)
        instance.accommodations = validated_data.get('accommodations', instance.accommodations)
        instance.activity_duration = validated_data.get('activity_duration', instance.activity_duration)
        instance.max_altitude = validated_data.get('max_altitude', instance.max_altitude)
        instance.youtubeUrl = validated_data.get('youtubeUrl', instance.youtubeUrl)
        instance.mapUrl = validated_data.get('mapUrl', instance.mapUrl)
        instance.pdfManual = validated_data.get('pdfManual', instance.pdfManual)
        instance.equipment = validated_data.get('equipment', instance.equipment)
        instance.save()

        # Handle nested updates without deletion
        faqs_data = validated_data.pop('faqs', [])
        highlights_data = validated_data.pop('highlights', [])
        gallery_data = validated_data.pop('gallery', [])
        videos_data = validated_data.pop('videos', [])
        inclusions_data = validated_data.pop('inclusions', [])
        exclusions_data = validated_data.pop('exclusions', [])
        notices_data = validated_data.pop('notices', [])
        dates_data = validated_data.pop('dates', [])

        # Update or create related objects
        self.update_or_create_related_objects(instance, HolidaysPackagesFaq, faqs_data, 'faqs')
        self.update_or_create_related_objects(instance, HolidaysPackagesHighlights, highlights_data, 'highlights')
        self.update_or_create_related_objects(instance, HolidaysPackagesGallery, gallery_data, 'gallery')
        self.update_or_create_related_objects(instance, HolidaysPackagesVideos, videos_data, 'videos')
        self.update_or_create_related_objects(instance, HolidaysPackagesInclusion, inclusions_data, 'inclusions')
        self.update_or_create_related_objects(instance, HolidaysPackagesExclusion, exclusions_data, 'exclusions')
        self.update_or_create_related_objects(instance, HolidaysPackagesNotice, notices_data, 'notices')
        self.update_or_create_related_objects(instance, HolidaysPackagesDates, dates_data, 'dates')

        return instance

    def update_or_create_related_objects(self, instance, model_class, data, related_name):
        existing_objects = {obj.id: obj for obj in getattr(instance, related_name).all()}
        for item_data in data:
            item_id = item_data.get('id')
            if item_id and item_id in existing_objects:
                # Update existing object
                item = existing_objects.pop(item_id)
                for attr, value in item_data.items():
                    setattr(item, attr, value)
                item.save()
            else:
                # Create new object
                model_class.objects.create(package=instance, **item_data)
        
        # Optionally, delete objects that are no longer referenced
        for old_object in existing_objects.values():
            old_object.delete()



class HolidaysPackagesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesType
        fields = '__all__'
        ref_name = 'HolidaysPackagesType'


# serializers.py



# serializers.py

from .models import HolidaysPackages

class HolidaysPackagesListSerializer(serializers.ModelSerializer):
    packagetype = HolidaysPackagesTypeSerializer(read_only=True)
    category = HolidaysPackagesCategorySerializer(read_only=True)

    class Meta:
        model = HolidaysPackages
        fields = [
            'id', 'country', 'city', 'packagetype', 'category', 'ordering', 'name', 
            'slug', 'description', 'image', 'price', 'destination', 'duration', 
            'start_point', 'end_point', 'group_size', 'season', 'meals', 
            'select_package_type', 'accommodations', 'activity_duration'
        ]






class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['id', 'name', 'ordering', 'slug', 'image']
        ref_name = 'Citie'



class CountriesSerializer(serializers.ModelSerializer):
    cities = CitiesSerializer(many=True, read_only=True)

    class Meta:
        model = Countries
        fields = ['id', 'continent', 'name', 'ordering', 'slug', 'image', 'cities']
        ref_name = 'Country'



class HolidaysPackagesCitySerializer(serializers.ModelSerializer):
    country = CountriesSerializer(read_only=True)
    city = CitiesSerializer(read_only=True)
    # packagetype = HolidaysPackagesTypeSerializer(read_only=True)
    # category = HolidaysPackagesCategorySerializer(read_only=True)

    class Meta:
        model = HolidaysPackages
        fields = ['id', 'country', 'city', 'packagetype', 'category', 'ordering', 'name', 'slug', 'description', 'image', 'price', 'destination', 'duration', 'start_point', 'end_point', 'group_size', 'season', 'meals', 'select_package_type', 'accommodations', 'activity_duration', 'max_altitude', 'youtubeUrl', 'mapUrl', 'pdfManual', 'description', 'equipment']


class HolidaysPackagesDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysPackagesDates
        fields = ['start_date', 'end_date']
        ref_name = 'HolidaysPackagesDatesSerializer_v1' 




class PackageDatesView(generics.GenericAPIView):
    serializer_class = HolidaysPackagesDatesSerializer

    def get(self, request, *args, **kwargs):
        package_id = self.kwargs.get('package_id')
        year = int(request.query_params.get('year'))
        month = int(request.query_params.get('month'))

        # Ensure the package exists
        try:
            package_dates = HolidaysPackagesDates.objects.filter(
                package_id=package_id,
                start_date__year=year,
                start_date__month=month
            )
        except HolidaysPackagesDates.DoesNotExist:
            return Response({'error': 'No dates found for the specified package and time'}, status=404)

        serializer = self.get_serializer(package_dates, many=True)
        return Response(serializer.data)
