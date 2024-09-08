from django.urls import path
from .views import *

urlpatterns = [
    path('categories/list/', HolidaysPackagesCategoryList.as_view(), name='categories_list'),
    path('categories/create/', HolidaysPackagesCategoryCreate.as_view(), name='create_category'),
    path('categories/detail/<uuid:pk>/', HolidaysPackagesCategoryDetail.as_view(), name='category_detail'),
    path('categories/update/<uuid:pk>/', HolidaysPackagesCategoryUpdate.as_view(), name='category_update'),
    path('categories/delete/<uuid:pk>/', HolidaysPackagesCategoryDelete.as_view(), name='category_delete'),

    path('holidays-packages/<uuid:pk>/', HolidaysPackagesUpdateView.as_view(), name='category_delete'),
    path('holidays-packages/', HolidaysPackagesCreateView.as_view(), name='holidays-packages-create'),
    path('holidays-packages/delete/<uuid:pk>/', HolidaysPackagesDeleteView.as_view(), name='holidays-packages-delete'),


    path('itinerary/<uuid:pk>/', HolidaysPackagesItineraryUpdateView.as_view(), name='holidays-packages-update'),
    path('itinerary/<uuid:pk>/', HolidaysPackageItinerarysDeleteView.as_view(), name='holidays-packages-delete'),
    path('itinerary', HolidaysPackagesItineraryView.as_view(), name='category_delete'),
    # path('itinerary/<uuid:pk>/', HolidaysPackagesItineraryView.as_view(), name='itinerary-update'),

    # HolidaysPackagesType
    path('type/create/', HolidaysPackagesTypeCreate.as_view(), name='create_type'),
    path('type/list/', HolidaysPackagesTypeList.as_view(), name='type_list'),
    path('type/detail/<slug:slug>/', HolidaysPackagesTypeDetail.as_view(), name='type_detail'),
    path('type/update/<uuid:pk>/', HolidaysPackagesTypeUpdate.as_view(), name='type_update'),
    path('type/delete/<uuid:pk>/', HolidaysPackagesTypeDelete.as_view(), name='type_delete'),

    # PackagesAccommodationDelete
    # path('accomondation/delete/<uuid:pk>/', PackagesAccommodationDelete.as_view(), name='accomondation_delete'),

    # HolidaysPackages type and category
    path('holiday-packages/types/', HolidaysPackagesTypeListView.as_view(), name='holiday-packages-types-list'),

    # holicays packages list -type-category
    path('holiday-all-type-category-packages/', HolidaysPackagesListView.as_view(), name='holiday-packages-list'),

    # get packages by category slug
    path('holiday-packages/category/<slug:slug>/', HolidaysPackagesByCategoryView.as_view(), name='holiday-packages-by-category'),

    # get packages by type slug
    path('holiday-packages/type/<slug:slug>/', HolidaysPackagesByTypeView.as_view(), name='holiday-packages-by-type'),


    # get packages by packages slug
    path('holiday-packages/detail/<slug:slug>/', HolidaysPackagesDetailView.as_view(), name='holiday-packages-detail'),


    path('categories/type/<slug:slug>/', CategoriesByTypeView.as_view(), name='categories-by-type'),




    path('countries-and-cities/', CountriesListView.as_view(), name='countries-list'),

    path('country-and-cities', PackagesListByCountryAndCity.as_view(), name='cities-list'),

    path('holiday-packages/country/<slug:slug>/', HolidaysPackagesByCountryView.as_view(), name='holiday-packages-by-country'),

    path('holiday-packages/city/<slug:slug>/', HolidaysPackagesByCityView.as_view(), name='holiday-packages-by-city'),


    path('cities/country/<slug:slug>/', CitiesByCountryView.as_view(), name='cities-by-country'),


    path('holiday-packages/filter/', HolidayPackagesInternaionalListView.as_view(), name='holiday-packages-list'),

    path('internation-domestic-countries-cities/', CountriesandCitiesListView.as_view(), name='countries-list'),


    path('packages/<uuid:package_id>/dates/', PackageDatesView.as_view(), name='package-dates'),













]
