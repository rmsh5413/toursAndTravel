from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from rest_framework import generics
from .models import *
from .serializers import *

class HolidaysPackagesItineraryUpdateView(generics.RetrieveUpdateAPIView):
    queryset = HolidaysPackagesItinerary.objects.all()
    serializer_class = UpdateHolidaysPackagesItinerarySerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": "Itinerary updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HolidaysPackageItinerarysDeleteView(generics.DestroyAPIView):
    queryset = HolidaysPackagesItinerary.objects.all()
    serializer_class = UpdateHolidaysPackagesItinerarySerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "success": "Package Itinerary deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
    

class HolidaysPackagesItineraryView(generics.ListCreateAPIView):
    queryset = HolidaysPackagesItinerary.objects.all()
    serializer_class = HolidaysPackagesItinerarySerializer

    def create(self, request, *args, **kwargs):
        serializer = HolidaysPackagesItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": "Package Itinerary created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class 




class PackagesAccommodationDelete(generics.DestroyAPIView):
    queryset = PackagesAccommodation.objects.all()
    serializer_class = PackagesAccommodationSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "success": "Accommodation deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "error": "Failed to delete accommodation", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        

class PackagesMealsDelete(generics.DestroyAPIView):
    queryset = PackagesMeals.objects.all()
    serializer_class = PackagesMealsSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "success": "Meals deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "error": "Failed to delete meals", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        


class PackagesActivitiesDelete(generics.DestroyAPIView):
    queryset = PackagesActivities.objects.all()
    serializer_class = PackagesActivitiesSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "success": "Activities deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "error": "Failed to delete activities", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        
