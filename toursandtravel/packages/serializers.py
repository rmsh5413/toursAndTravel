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
    




from rest_framework import serializers
from .models import (
    HolidaysPackages,
    HolidaysPackagesItinerary,
    PackagesAccommodation,
    PackagesMeals,
    PackagesActivities
)

# class PackagesAccommodationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PackagesAccommodation
#         fields = ['id', 'title']

# class PackagesMealsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PackagesMeals
#         fields = ['id', 'title']

# class PackagesActivitiesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PackagesActivities
#         fields = ['id', 'title']

# class HolidaysPackagesItinerarySerializer(serializers.ModelSerializer):
#     accommodation = PackagesAccommodationSerializer(many=True, required=False)
#     meals = PackagesMealsSerializer(many=True, required=False)
#     activities = PackagesActivitiesSerializer(many=True, required=False)

#     class Meta:
#         model = HolidaysPackagesItinerary
#         fields = ['id', 'day', 'title', 'description', 'image', 'accommodation', 'meals', 'activities']

# class HolidaysPackagesSerializer(serializers.ModelSerializer):
#     itinerary = HolidaysPackagesItinerarySerializer(many=True, required=False)

#     class Meta:
#         model = HolidaysPackages
#         fields = [
#             'id', 'packagetype', 'category', 'ordering', 'name', 'slug', 'description',
#             'image', 'price', 'destination', 'duration', 'start_point', 'end_point',
#             'group_size', 'season', 'meals', 'select_package_type', 'accommodations',
#             'activity_duration', 'max_altitude', 'youtubeUrl', 'mapUrl', 'pdfManual',
#             'itinerary'
#         ]

#     def update(self, instance, validated_data):
#         # Update HolidaysPackages fields
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.save()

#         # Handle nested itineraries
#         itineraries_data = validated_data.pop('itinerary', [])
#         for itinerary_data in itineraries_data:
#             itinerary_id = itinerary_data.get('id')
#             if itinerary_id:
#                 itinerary = HolidaysPackagesItinerary.objects.get(id=itinerary_id, package=instance)
#                 itinerary.day = itinerary_data.get('day', itinerary.day)
#                 itinerary.title = itinerary_data.get('title', itinerary.title)
#                 itinerary.description = itinerary_data.get('description', itinerary.description)
#                 itinerary.image = itinerary_data.get('image', itinerary.image)
#                 itinerary.save()
#             else:
#                 itinerary = HolidaysPackagesItinerary.objects.create(package=instance, **itinerary_data)

#             # Handle accommodations for the itinerary
#             accommodations_data = itinerary_data.pop('accommodation', [])
#             for accommodation_data in accommodations_data:
#                 accommodation_id = accommodation_data.get('id')
#                 if accommodation_id:
#                     accommodation = PackagesAccommodation.objects.get(id=accommodation_id, itinerary=itinerary)
#                     accommodation.title = accommodation_data.get('title', accommodation.title)
#                     accommodation.save()
#                 else:
#                     PackagesAccommodation.objects.create(itinerary=itinerary, **accommodation_data)

#             # Handle meals for the itinerary
#             meals_data = itinerary_data.pop('meals', [])
#             for meal_data in meals_data:
#                 meal_id = meal_data.get('id')
#                 if meal_id:
#                     meal = PackagesMeals.objects.get(id=meal_id, itinerary=itinerary)
#                     meal.title = meal_data.get('title', meal.title)
#                     meal.save()
#                 else:
#                     PackagesMeals.objects.create(itinerary=itinerary, **meal_data)

#             # Handle activities for the itinerary
#             activities_data = itinerary_data.pop('activities', [])
#             for activity_data in activities_data:
#                 activity_id = activity_data.get('id')
#                 if activity_id:
#                     activity = PackagesActivities.objects.get(id=activity_id, itinerary=itinerary)
#                     activity.title = activity_data.get('title', activity.title)
#                     activity.save()
#                 else:
#                     PackagesActivities.objects.create(itinerary=itinerary, **activity_data)

#         return instance



from rest_framework import serializers
from .models import (
    HolidaysPackagesItinerary,
    PackagesAccommodation,
    PackagesMeals,
    PackagesActivities
)

class PackagesAccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackagesAccommodation
        fields = ['id', 'itinerary', 'title']

class PackagesMealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackagesMeals
        fields = ['id', 'itinerary', 'title']

class PackagesActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackagesActivities
        fields = ['id', 'itinerary', 'title']

class HolidaysPackagesItinerarySerializer(serializers.ModelSerializer):
    accommodation = PackagesAccommodationSerializer(many=True, required=False)
    meals = PackagesMealsSerializer(many=True, required=False)
    activities = PackagesActivitiesSerializer(many=True, required=False)

    class Meta:
        model = HolidaysPackagesItinerary
        fields = ['id', 'day', 'title', 'description', 'image', 'accommodation', 'meals', 'activities']

    def create(self, validated_data):
        accommodations_data = validated_data.pop('accommodation', [])
        meals_data = validated_data.pop('meals', [])
        activities_data = validated_data.pop('activities', [])
        
        itinerary = HolidaysPackagesItinerary.objects.create(**validated_data)

        # Create related objects
        for accommodation_data in accommodations_data:
            PackagesAccommodation.objects.create(itinerary=itinerary, **accommodation_data)
        
        for meal_data in meals_data:
            PackagesMeals.objects.create(itinerary=itinerary, **meal_data)
        
        for activity_data in activities_data:
            PackagesActivities.objects.create(itinerary=itinerary, **activity_data)

        return itinerary
    

# class UpdateHolidaysPackagesItinerarySerializer(serializers.ModelSerializer):
#     accommodation = PackagesAccommodationSerializer(many=True, required=False)
#     meals = PackagesMealsSerializer(many=True, required=False)
#     activities = PackagesActivitiesSerializer(many=True, required=False)

#     class Meta:
#         model = HolidaysPackagesItinerary
#         fields = ['id', 'day', 'title', 'description', 'image', 'accommodation', 'meals', 'activities']


#     def update(self, instance, validated_data):
#         accommodations_data = validated_data.pop('accommodation', [])
#         meals_data = validated_data.pop('meals', [])
#         activities_data = validated_data.pop('activities', [])
        
#         # instance.ordering = validated_data.get('ordering', instance.ordering)
#         instance.day = validated_data.get('day', instance.day)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.image = validated_data.get('image', instance.image)
#         instance.save()

#         # Update or create related objects
#         for accommodation_data in accommodations_data:
#             accommodation_id = accommodation_data.get('id')
#             if accommodation_id:
#                 accommodation = PackagesAccommodation.objects.get(id=accommodation_id, itinerary=instance)
#                 accommodation.title = accommodation_data.get('title', accommodation.title)
#                 accommodation.save()
#             else:
#                 PackagesAccommodation.objects.create(itinerary=instance, **accommodation_data)

#         for meal_data in meals_data:
#             meal_id = meal_data.get('id')
#             if meal_id:
#                 meal = PackagesMeals.objects.get(id=meal_id, itinerary=instance)
#                 meal.title = meal_data.get('title', meal.title)
#                 meal.save()
#             else:
#                 PackagesMeals.objects.create(itinerary=instance, **meal_data)

#         for activity_data in activities_data:
#             activity_id = activity_data.get('id')
#             if activity_id:
#                 activity = PackagesActivities.objects.get(id=activity_id, itinerary=instance)
#                 activity.title = activity_data.get('title', activity.title)
#                 activity.save()
#             else:
#                 PackagesActivities.objects.create(itinerary=instance, **activity_data)

#         return instance


# class UpdateHolidaysPackagesItinerarySerializer(serializers.ModelSerializer):
#     accommodation = PackagesAccommodationSerializer(many=True, required=False)
#     meals = PackagesMealsSerializer(many=True, required=False)
#     activities = PackagesActivitiesSerializer(many=True, required=False)

#     class Meta:
#         model = HolidaysPackagesItinerary
#         fields = ['id', 'day', 'title', 'description', 'image', 'accommodation', 'meals', 'activities']

#     def update(self, instance, validated_data):
#         accommodations_data = validated_data.pop('accommodation', [])
#         meals_data = validated_data.pop('meals', [])
#         activities_data = validated_data.pop('activities', [])

#         instance.day = validated_data.get('day', instance.day)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.image = validated_data.get('image', instance.image)
#         instance.save()

#         # Handle accommodation update or creation
#         current_accommodations = {accommodation.id: accommodation for accommodation in instance.accommodation.all()}
#         updated_accommodations = []

#         for accommodation_data in accommodations_data:
#             accommodation_id = accommodation_data.get('id')
#             if accommodation_id and accommodation_id in current_accommodations:
#                 accommodation = current_accommodations.pop(accommodation_id)
#                 accommodation.title = accommodation_data.get('title', accommodation.title)
#                 accommodation.save()
#                 updated_accommodations.append(accommodation.id)
#             else:
#                 new_accommodation = PackagesAccommodation.objects.create(itinerary=instance, **accommodation_data)
#                 updated_accommodations.append(new_accommodation.id)

#         # Delete accommodations that were not updated
#         PackagesAccommodation.objects.filter(itinerary=instance).exclude(id__in=updated_accommodations).delete()

#         # Handle meals update or creation
#         current_meals = {meal.id: meal for meal in instance.meals.all()}
#         updated_meals = []

#         for meal_data in meals_data:
#             meal_id = meal_data.get('id')
#             if meal_id and meal_id in current_meals:
#                 meal = current_meals.pop(meal_id)
#                 meal.title = meal_data.get('title', meal.title)
#                 meal.save()
#                 updated_meals.append(meal.id)
#             else:
#                 new_meal = PackagesMeals.objects.create(itinerary=instance, **meal_data)
#                 updated_meals.append(new_meal.id)

#         # Delete meals that were not updated
#         PackagesMeals.objects.filter(itinerary=instance).exclude(id__in=updated_meals).delete()

#         # Handle activities update or creation
#         current_activities = {activity.id: activity for activity in instance.activities.all()}
#         updated_activities = []

#         for activity_data in activities_data:
#             activity_id = activity_data.get('id')
#             if activity_id and activity_id in current_activities:
#                 activity = current_activities.pop(activity_id)
#                 activity.title = activity_data.get('title', activity.title)
#                 activity.save()
#                 updated_activities.append(activity.id)
#             else:
#                 new_activity = PackagesActivities.objects.create(itinerary=instance, **activity_data)
#                 updated_activities.append(new_activity.id)

#         # Delete activities that were not updated
#         PackagesActivities.objects.filter(itinerary=instance).exclude(id__in=updated_activities).delete()

#         return instance
# class UpdateHolidaysPackagesItinerarySerializer(serializers.ModelSerializer):
#     accommodation = PackagesAccommodationSerializer(many=True, required=False)
#     meals = PackagesMealsSerializer(many=True, required=False)
#     activities = PackagesActivitiesSerializer(many=True, required=False)

#     class Meta:
#         model = HolidaysPackagesItinerary
#         fields = ['id', 'day', 'title', 'description', 'image', 'accommodation', 'meals', 'activities']

#     def update(self, instance, validated_data):
#         accommodations_data = validated_data.pop('accommodation', [])
#         meals_data = validated_data.pop('meals', [])
#         activities_data = validated_data.pop('activities', [])

#         instance.day = validated_data.get('day', instance.day)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.image = validated_data.get('image', instance.image)
#         instance.save()

#         # Handle accommodation update or creation
#         for accommodation_data in accommodations_data:
#             accommodation_id = accommodation_data.get('id')
#             if accommodation_id:
#                 # Update existing accommodation
#                 accommodation = PackagesAccommodation.objects.get(id=accommodation_id, itinerary=instance)
#                 accommodation.title = accommodation_data.get('title', accommodation.title)
#                 accommodation.save()
#             else:
#                 # Create new accommodation
#                 PackagesAccommodation.objects.create(itinerary=instance, **accommodation_data)

#         # Handle meals update or creation
#         for meal_data in meals_data:
#             meal_id = meal_data.get('id')
#             if meal_id:
#                 # Update existing meal
#                 meal = PackagesMeals.objects.get(id=meal_id, itinerary=instance)
#                 meal.title = meal_data.get('title', meal.title)
#                 meal.save()
#             else:
#                 # Create new meal
#                 PackagesMeals.objects.create(itinerary=instance, **meal_data)

#         # Handle activities update or creation
#         for activity_data in activities_data:
#             activity_id = activity_data.get('id')
#             if activity_id:
#                 # Update existing activity
#                 activity = PackagesActivities.objects.get(id=activity_id, itinerary=instance)
#                 activity.title = activity_data.get('title', activity.title)
#                 activity.save()
#             else:
#                 # Create new activity
#                 PackagesActivities.objects.create(itinerary=instance, **activity_data)

#         return instance


class UpdateHolidaysPackagesItinerarySerializer(serializers.ModelSerializer):
    accommodation = PackagesAccommodationSerializer(many=True, required=False)
    meals = PackagesMealsSerializer(many=True, required=False)
    activities = PackagesActivitiesSerializer(many=True, required=False)

    class Meta:
        model = HolidaysPackagesItinerary
        fields = ['id', 'day', 'title', 'description', 'image', 'accommodation', 'meals', 'activities']

    def update(self, instance, validated_data):
        # Extract nested data
        accommodations_data = validated_data.pop('accommodation', [])
        meals_data = validated_data.pop('meals', [])
        activities_data = validated_data.pop('activities', [])

        # Update the instance fields
        instance.day = validated_data.get('day', instance.day)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        # Update or create accommodations
        existing_accommodations = {accommodation.id: accommodation for accommodation in instance.accommodation.all()}
        for accommodation_data in accommodations_data:
            accommodation_id = accommodation_data.get('id')
            if accommodation_id and accommodation_id in existing_accommodations:
                # Update existing accommodation
                accommodation = existing_accommodations.pop(accommodation_id)
                for attr, value in accommodation_data.items():
                    setattr(accommodation, attr, value)
                accommodation.save()
            else:
                # Create new accommodation
                PackagesAccommodation.objects.create(itinerary=instance, **accommodation_data)

        # Update or create meals
        existing_meals = {meal.id: meal for meal in instance.meals.all()}
        for meal_data in meals_data:
            meal_id = meal_data.get('id')
            if meal_id and meal_id in existing_meals:
                # Update existing meal
                meal = existing_meals.pop(meal_id)
                for attr, value in meal_data.items():
                    setattr(meal, attr, value)
                meal.save()
            else:
                # Create new meal
                PackagesMeals.objects.create(itinerary=instance, **meal_data)

        # Update or create activities
        existing_activities = {activity.id: activity for activity in instance.activities.all()}
        for activity_data in activities_data:
            activity_id = activity_data.get('id')
            if activity_id and activity_id in existing_activities:
                # Update existing activity
                activity = existing_activities.pop(activity_id)
                for attr, value in activity_data.items():
                    setattr(activity, attr, value)
                activity.save()
            else:
                # Create new activity
                PackagesActivities.objects.create(itinerary=instance, **activity_data)

        # Remove outdated objects (if necessary)
        # Remove accommodation that was not updated or created
        for old_accommodation in existing_accommodations.values():
            old_accommodation.delete()
        
        # Remove meal that was not updated or created
        for old_meal in existing_meals.values():
            old_meal.delete()
        
        # Remove activity that was not updated or created
        for old_activity in existing_activities.values():
            old_activity.delete()

        return instance


# class UpdateHolidaysPackagesItinerarySerializer(serializers.ModelSerializer):
#     accommodation = PackagesAccommodationSerializer(many=True, required=False)
#     meals = PackagesMealsSerializer(many=True, required=False)
#     activities = PackagesActivitiesSerializer(many=True, required=False)

#     class Meta:
#         model = HolidaysPackagesItinerary
#         fields = ['id', 'day', 'title', 'description', 'image', 'accommodation', 'meals', 'activities']

#     def update(self, instance, validated_data):
#         accommodations_data = validated_data.pop('accommodation', [])
#         meals_data = validated_data.pop('meals', [])
#         activities_data = validated_data.pop('activities', [])
        
#         # Update instance fields
#         instance.day = validated_data.get('day', instance.day)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.image = validated_data.get('image', instance.image)
#         instance.save()

#         # Update or create accommodations
#         existing_accommodation_ids = [accommodation.id for accommodation in instance.accommodation.all()]
#         new_accommodation_ids = [accommodation_data.get('id') for accommodation_data in accommodations_data if accommodation_data.get('id')]

#         # Delete accommodations that are not in the new data
#         for accommodation_id in existing_accommodation_ids:
#             if accommodation_id not in new_accommodation_ids:
#                 PackagesAccommodation.objects.filter(id=accommodation_id, itinerary=instance).delete()

#         for accommodation_data in accommodations_data:
#             accommodation_id = accommodation_data.get('id')
#             if accommodation_id:
#                 accommodation = PackagesAccommodation.objects.get(id=accommodation_id, itinerary=instance)
#                 accommodation.title = accommodation_data.get('title', accommodation.title)
#                 accommodation.save()
#             else:
#                 PackagesAccommodation.objects.create(itinerary=instance, **accommodation_data)

#         # Update or create meals
#         existing_meal_ids = [meal.id for meal in instance.meals.all()]
#         new_meal_ids = [meal_data.get('id') for meal_data in meals_data if meal_data.get('id')]

#         # Delete meals that are not in the new data
#         for meal_id in existing_meal_ids:
#             if meal_id not in new_meal_ids:
#                 PackagesMeals.objects.filter(id=meal_id, itinerary=instance).delete()

#         for meal_data in meals_data:
#             meal_id = meal_data.get('id')
#             if meal_id:
#                 meal = PackagesMeals.objects.get(id=meal_id, itinerary=instance)
#                 meal.title = meal_data.get('title', meal.title)
#                 meal.save()
#             else:
#                 PackagesMeals.objects.create(itinerary=instance, **meal_data)

#         # Update or create activities
#         existing_activity_ids = [activity.id for activity in instance.activities.all()]
#         new_activity_ids = [activity_data.get('id') for activity_data in activities_data if activity_data.get('id')]

#         # Delete activities that are not in the new data
#         for activity_id in existing_activity_ids:
#             if activity_id not in new_activity_ids:
#                 PackagesActivities.objects.filter(id=activity_id, itinerary=instance).delete()

#         for activity_data in activities_data:
#             activity_id = activity_data.get('id')
#             if activity_id:
#                 activity = PackagesActivities.objects.get(id=activity_id, itinerary=instance)
#                 activity.title = activity_data.get('title', activity.title)
#                 activity.save()
#             else:
#                 PackagesActivities.objects.create(itinerary=instance, **activity_data)

#         return instance
