from rest_framework import serializers
from .models import *


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


