


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
#                 activity = PackagesActivities.objects.get(id=activity_id, itinerary=instance)HolidaysPackagesDatesSerializer
#                 activity.title = activity_data.get('title', activity.title)
#                 activity.save()
#             else:
#                 PackagesActivities.objects.create(itinerary=instance, **activity_data)

#         return instance




