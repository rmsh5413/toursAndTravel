from django.urls import path
from .views import *

urlpatterns = [
 
    # Countries
    path('countries/create/', CountiresCreateView.as_view(), name='create_country'),
    path('countries/list/', CountriesListView.as_view(), name='countries_list'),
    path('countries/detail/<uuid:pk>/', CountriesDetailView.as_view(), name='countries_detail'),
    path('countries/update/<uuid:pk>/', CountriesUpdateView.as_view(), name='countries_update'),
    path('countries/delete/<uuid:pk>/', CountriesDeleteView.as_view(), name='countries_delete'),


    # Cities
    path('cities/create/', CitiesCreateView.as_view(), name='create_city'),
    path('cities/list/', CitiesListView.as_view(), name='cities_list'),
    path('cities/detail/<uuid:pk>/', CitiesDetailView.as_view(), name='cities_detail'),
    path('cities/update/<uuid:pk>/', CitiesUpdateView.as_view(), name='cities_update'),
    path('cities/delete/<uuid:pk>/', CitiesDeleteView.as_view(), name='cities_delete'),

]