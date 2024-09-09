from django.urls import path
from .views import *

urlpatterns = [

    path('holidays-packages/<uuid:pk>/', HolidaysPackagesUpdateView.as_view(), name='category_delete'),
    path('holidays-packages/', HolidaysPackagesCreateView.as_view(), name='holidays-packages-create'),
    path('holidays-packages/delete/<uuid:pk>/', HolidaysPackagesDeleteView.as_view(), name='holidays-packages-delete'),



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


    # HolidaysPackagesInclusionDelete
    path('inclusion/delete/<uuid:pk>/', HolidaysPackagesInclusionDelete.as_view(), name='inclusion_delete'),

    # HolidaysPackagesExclusionDelete
    path('exclusion/delete/<uuid:pk>/', HolidaysPackagesExclusionDelete.as_view(), name='exclusion_delete'),

    # HolidaysPackagesNoticeDelete
    path('notice/delete/<uuid:pk>/', HolidaysPackagesNoticeDelete.as_view(), name='notice_delete'),

    # HolidaysPackagesDates
    path('dates/delete/<uuid:pk>/', HolidaysPackagesDatesDelete.as_view(), name='dates_delete'),

    # HolidaysPackagesFaqDelete
    path('faq/delete/<uuid:pk>/', HolidaysPackagesFaqDelete.as_view(), name='faq_delete'),

    # HolidaysPackagesComments
    path('comments/create/', HolidaysPackagesCommentsCreate.as_view(), name='comments_create'),
    path('comments/list/', HolidaysPackagesCommentsList.as_view(), name='comments_list'),
    path('comments/detail/<uuid:pk>/', HolidaysPackagesCommentsDetail.as_view(), name='comments_detail'),
    path('comments/delete/<uuid:pk>/', HolidaysPackagesCommentsDelete.as_view(), name='comments_delete'),

    # HolidaysPackagesHighlightsDelete
    path('highlights/delete/<uuid:pk>/', HolidaysPackagesHighlightsDelete.as_view(), name='highlights_delete'),

    # HolidaysPackagesGalleryDelete

    # HolidaysPackagesVideosDelete










]
