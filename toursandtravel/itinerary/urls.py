from django.urls import path
from .views import *

urlpatterns = [
    path('itinerary/<uuid:pk>/', HolidaysPackagesItineraryUpdateView.as_view(), name='holidays-packages-update'),
    path('itinerary/<uuid:pk>/', HolidaysPackageItinerarysDeleteView.as_view(), name='holidays-packages-delete'),
    path('itinerary', HolidaysPackagesItineraryView.as_view(), name='category_delete'),
    # path('itinerary/<uuid:pk>/', HolidaysPackagesItineraryView.as_view(), name='itinerary-update'),

   

     # PackagesAccommodationDelete
    path('accomondation/delete/<uuid:pk>/', PackagesAccommodationDelete.as_view(), name='accomondation_delete'),

    # PackagesMealsDelete
    path('meals/delete/<uuid:pk>/', PackagesMealsDelete.as_view(), name='meals_delete'),

    # PackagesActivitiesDelete
    path('activities/delete/<uuid:pk>/', PackagesActivitiesDelete.as_view(), name='activities_delete'),








]
