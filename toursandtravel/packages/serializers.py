from rest_framework import serializers
from .models import *
from gallery.models import *
from videos.models import *

from comments.models import HolidaysPackagesComments


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

# class UpdateHolidaysPackagesSerializer(serializers.ModelSerializer):
#     faqs = HolidaysPackagesFaqSerializer(many=True, required=False)
#     highlights = HolidaysPackagesHighlightsSerializer(many=True, required=False)
#     gallery = HolidaysPackagesGallerySerializer(many=True, required=False)
#     videos = HolidaysPackagesVideosSerializer(many=True, required=False)
#     inclusions = HolidaysPackagesInclusionSerializer(many=True, required=False)
#     exclusions = HolidaysPackagesExclusionSerializer(many=True, required=False)
#     notices = HolidaysPackagesNoticeSerializer(many=True, required=False)
#     dates = HolidaysPackagesDatesSerializer(many=True, required=False)

#     class Meta:
#         model = HolidaysPackages
#         fields = [
#             'id', 'country', 'city', 'packagetype', 'category', 'ordering', 'name', 'slug', 'description',
#             'image', 'price', 'destination', 'duration', 'start_point', 'end_point',
#             'group_size', 'season', 'meals', 'select_package_type', 'accommodations',
#             'activity_duration', 'max_altitude', 'youtubeUrl', 'mapUrl', 'pdfManual',
#             'faqs', 'highlights', 'gallery', 'videos', 'inclusions', 'exclusions', 'notices', 'dates'
#         ]

#     def update(self, instance, validated_data):
#         # Update HolidaysPackages fields
#         instance.name = validated_data.get('name', instance.name)
#         instance.country = validated_data.get('country', instance.country)
#         instance.city = validated_data.get('city', instance.city)
#         instance.image = validated_data.get('image', instance.image)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.destination = validated_data.get('destination', instance.destination)
#         instance.duration = validated_data.get('duration', instance.duration)
#         instance.start_point = validated_data.get('start_point', instance.start_point)
#         instance.end_point = validated_data.get('end_point', instance.end_point)
#         instance.group_size = validated_data.get('group_size', instance.group_size)
#         instance.season = validated_data.get('season', instance.season)
#         instance.meals = validated_data.get('meals', instance.meals)
#         instance.select_package_type = validated_data.get('select_package_type', instance.select_package_type)
#         instance.accommodations = validated_data.get('accommodations', instance.accommodations)
#         instance.activity_duration = validated_data.get('activity_duration', instance.activity_duration)
#         instance.max_altitude = validated_data.get('max_altitude', instance.max_altitude)
#         instance.youtubeUrl = validated_data.get('youtubeUrl', instance.youtubeUrl)
#         instance.mapUrl = validated_data.get('mapUrl', instance.mapUrl)
#         instance.pdfManual = validated_data.get('pdfManual', instance.pdfManual)
#         instance.equipment = validated_data.get('equipment', instance.equipment)
#         instance.save()

#         # Handle nested updates without deletion
#         faqs_data = validated_data.pop('faqs', [])
#         highlights_data = validated_data.pop('highlights', [])
#         gallery_data = validated_data.pop('gallery', [])
#         videos_data = validated_data.pop('videos', [])
#         inclusions_data = validated_data.pop('inclusions', [])
#         exclusions_data = validated_data.pop('exclusions', [])
#         notices_data = validated_data.pop('notices', [])
#         dates_data = validated_data.pop('dates', [])

#         # Update or create related objects
#         for faq_data in faqs_data:
#             faq_id = faq_data.get('id')
#             if faq_id:
#                 faq = HolidaysPackagesFaq.objects.get(id=faq_id, package=instance)
#                 faq.question = faq_data.get('question', faq.question)
#                 faq.answer = faq_data.get('answer', faq.answer)
#                 faq.save()
#             else:
#                 HolidaysPackagesFaq.objects.create(package=instance, **faq_data)

#         for highlight_data in highlights_data:
#             highlight_id = highlight_data.get('id')
#             if highlight_id:
#                 highlight = HolidaysPackagesHighlights.objects.get(id=highlight_id, package=instance)
#                 highlight.detail = highlight_data.get('detail', highlight.detail)
#                 highlight.save()
#             else:
#                 HolidaysPackagesHighlights.objects.create(package=instance, **highlight_data)

#         for gallery_data_item in gallery_data:
#             gallery_id = gallery_data_item.get('id')
#             if gallery_id:
#                 gallery = HolidaysPackagesGallery.objects.get(id=gallery_id, package=instance)
#                 gallery.image = gallery_data_item.get('image', gallery.image)
#                 gallery.save()
#             else:
#                 HolidaysPackagesGallery.objects.create(package=instance, **gallery_data_item)

#         for video_data in videos_data:
#             video_id = video_data.get('id')
#             if video_id:
#                 video = HolidaysPackagesVideos.objects.get(id=video_id, package=instance)
#                 video.video = video_data.get('video', video.video)
#                 video.save()
#             else:
#                 HolidaysPackagesVideos.objects.create(package=instance, **video_data)

#         for inclusion_data in inclusions_data:
#             inclusion_id = inclusion_data.get('id')
#             if inclusion_id:
#                 inclusion = HolidaysPackagesInclusion.objects.get(id=inclusion_id, package=instance)
#                 inclusion.detail = inclusion_data.get('detail', inclusion.detail)
#                 inclusion.save()
#             else:
#                 HolidaysPackagesInclusion.objects.create(package=instance, **inclusion_data)

#         for exclusion_data in exclusions_data:
#             exclusion_id = exclusion_data.get('id')
#             if exclusion_id:
#                 exclusion = HolidaysPackagesExclusion.objects.get(id=exclusion_id, package=instance)
#                 exclusion.detail = exclusion_data.get('detail', exclusion.detail)
#                 exclusion.save()
#             else:
#                 HolidaysPackagesExclusion.objects.create(package=instance, **exclusion_data)

#         for notice_data in notices_data:
#             notice_id = notice_data.get('id')
#             if notice_id:
#                 notice = HolidaysPackagesNotice.objects.get(id=notice_id, package=instance)
#                 notice.title = notice_data.get('title', notice.title)
#                 notice.description = notice_data.get('description', notice.description)
#                 notice.save()
#             else:
#                 HolidaysPackagesNotice.objects.create(package=instance, **notice_data)

#         for date_data in dates_data:
#             date_id = date_data.get('id')
#             if date_id:
#                 date = HolidaysPackagesDates.objects.get(id=date_id, package=instance)
#                 date.start_date = date_data.get('start_date', date.start_date)
#                 date.end_date = date_data.get('end_date', date.end_date)
#                 date.save()
#             else:
#                 HolidaysPackagesDates.objects.create(package=instance, **date_data)

#         return instance



# class UpdateHolidaysPackagesSerializer(serializers.ModelSerializer):
#     faqs = HolidaysPackagesFaqSerializer(many=True, required=False)
#     highlights = HolidaysPackagesHighlightsSerializer(many=True, required=False)
#     gallery = HolidaysPackagesGallerySerializer(many=True, required=False)
#     videos = HolidaysPackagesVideosSerializer(many=True, required=False)
#     inclusions = HolidaysPackagesInclusionSerializer(many=True, required=False)
#     exclusions = HolidaysPackagesExclusionSerializer(many=True, required=False)
#     notices = HolidaysPackagesNoticeSerializer(many=True, required=False)
#     dates = HolidaysPackagesDatesSerializer(many=True, required=False)

#     class Meta:
#         model = HolidaysPackages
#         fields = [
#             'id','country','city', 'packagetype', 'category', 'ordering', 'name', 'slug', 'description',
#             'image', 'price', 'destination', 'duration', 'start_point', 'end_point',
#             'group_size', 'season', 'meals', 'select_package_type', 'accommodations',
#             'activity_duration', 'max_altitude', 'youtubeUrl', 'mapUrl', 'pdfManual',
#             'faqs', 'highlights', 'gallery', 'videos', 'inclusions', 'exclusions', 'notices', 'dates'
#         ]

#     def update(self, instance, validated_data):
#         # Update the HolidaysPackages fields
#         instance.name = validated_data.get('name', instance.name)
#         instance.country = validated_data.get('country', instance.country)
#         instance.city = validated_data.get('city', instance.city)
#         instance.image = validated_data.get('image', instance.image)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.destination = validated_data.get('destination', instance.destination)
#         instance.duration = validated_data.get('duration', instance.duration)
#         instance.start_point = validated_data.get('start_point', instance.start_point)
#         instance.end_point = validated_data.get('end_point', instance.end_point)
#         instance.group_size = validated_data.get('group_size', instance.group_size)
#         instance.season = validated_data.get('season', instance.season)
#         instance.meals = validated_data.get('meals', instance.meals)
#         instance.select_package_type = validated_data.get('select_package_type', instance.select_package_type)
#         instance.accommodations = validated_data.get('accommodations', instance.accommodations)
#         instance.activity_duration = validated_data.get('activity_duration', instance.activity_duration)
#         instance.max_altitude = validated_data.get('max_altitude', instance.max_altitude)
#         instance.youtubeUrl = validated_data.get('youtubeUrl', instance.youtubeUrl)
#         instance.mapUrl = validated_data.get('mapUrl', instance.mapUrl)
#         instance.pdfManual = validated_data.get('pdfManual', instance.pdfManual)
#         instance.description = validated_data.get('description', instance.description)
#         instance.equipment = validated_data.get('equipment', instance.equipment)
#         instance.save()


#         # Handle nested updates
#         faqs_data = validated_data.pop('faqs', [])
#         highlights_data = validated_data.pop('highlights', [])
#         gallery_data = validated_data.pop('gallery', [])
#         videos_data = validated_data.pop('videos', [])
#         inclusions_data = validated_data.pop('inclusions', [])
#         exclusions_data = validated_data.pop('exclusions', [])
#         notices_data = validated_data.pop('notices', [])
#         dates_data = validated_data.pop('dates', [])

#         # Update or create related objects
#         for faq_data in faqs_data:
#             faq_id = faq_data.get('id')
#             if faq_id:
#                 faq = HolidaysPackagesFaq.objects.get(id=faq_id, package=instance)
#                 faq.question = faq_data.get('question', faq.question)
#                 faq.answer = faq_data.get('answer', faq.answer)
#                 faq.save()
#             else:
#                 HolidaysPackagesFaq.objects.create(package=instance, **faq_data)

#         for highlight_data in highlights_data:
#             highlight_id = highlight_data.get('id')
#             if highlight_id:
#                 highlight = HolidaysPackagesHighlights.objects.get(id=highlight_id, package=instance)
#                 highlight.detail = highlight_data.get('detail', highlight.detail)
#                 highlight.save()
#             else:
#                 HolidaysPackagesHighlights.objects.create(package=instance, **highlight_data)

#         for gallery_data_item in gallery_data:
#             gallery_id = gallery_data_item.get('id')
#             if gallery_id:
#                 gallery = HolidaysPackagesGallery.objects.get(id=gallery_id, package=instance)
#                 gallery.image = gallery_data_item.get('image', gallery.image)
#                 gallery.save()
#             else:
#                 HolidaysPackagesGallery.objects.create(package=instance, **gallery_data_item)

#         for video_data in videos_data:
#             video_id = video_data.get('id')
#             if video_id:
#                 video = HolidaysPackagesVideos.objects.get(id=video_id, package=instance)
#                 video.video = video_data.get('video', video.video)
#                 video.save()
#             else:
#                 HolidaysPackagesVideos.objects.create(package=instance, **video_data)

#         for inclusion_data in inclusions_data:
#             inclusion_id = inclusion_data.get('id')
#             if inclusion_id:
#                 inclusion = HolidaysPackagesInclusion.objects.get(id=inclusion_id, package=instance)
#                 inclusion.detail = inclusion_data.get('detail', inclusion.detail)
#                 inclusion.save()
#             else:
#                 HolidaysPackagesInclusion.objects.create(package=instance, **inclusion_data)

#         for exclusion_data in exclusions_data:
#             exclusion_id = exclusion_data.get('id')
#             if exclusion_id:
#                 exclusion = HolidaysPackagesExclusion.objects.get(id=exclusion_id, package=instance)
#                 exclusion.detail = exclusion_data.get('detail', exclusion.detail)
#                 exclusion.save()
#             else:
#                 HolidaysPackagesExclusion.objects.create(package=instance, **exclusion_data)

#         for notice_data in notices_data:
#             notice_id = notice_data.get('id')
#             if notice_id:
#                 notice = HolidaysPackagesNotice.objects.get(id=notice_id, package=instance)
#                 notice.title = notice_data.get('title', notice.title)
#                 notice.description = notice_data.get('description', notice.description)
#                 notice.save()
#             else:
#                 HolidaysPackagesNotice.objects.create(package=instance, **notice_data)

#         for date_data in dates_data:
#             date_id = date_data.get('id')
#             if date_id:
#                 date = HolidaysPackagesDates.objects.get(id=date_id, package=instance)
#                 date.start_date = date_data.get('start_date', date.start_date)
#                 date.end_date = date_data.get('end_date', date.end_date)
#                 date.save()
#             else:
#                 HolidaysPackagesDates.objects.create(package=instance, **date_data)

#         return instance
    



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





# serializers.py

from rest_framework import serializers
from .models import Cities

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['id', 'name', 'ordering', 'slug', 'image']


# serializers.py

from .models import Countries

class CountriesSerializer(serializers.ModelSerializer):
    cities = CitiesSerializer(many=True, read_only=True)

    class Meta:
        model = Countries
        fields = ['id', 'continent', 'name', 'ordering', 'slug', 'image', 'cities']



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


from rest_framework import generics
from rest_framework.response import Response
from .models import HolidaysPackagesDates
from .serializers import HolidaysPackagesDatesSerializer
from django.utils.dateparse import parse_date
from datetime import datetime

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
