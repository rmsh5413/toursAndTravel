from django.urls import path
from .views import *

urlpatterns = [

    path('categories/list/', HolidaysPackagesCategoryList.as_view(), name='categories_list'),
    path('categories/create/', HolidaysPackagesCategoryCreate.as_view(), name='create_category'),
    path('categories/detail/<uuid:pk>/', HolidaysPackagesCategoryDetail.as_view(), name='category_detail'),
    path('categories/update/<uuid:pk>/', HolidaysPackagesCategoryUpdate.as_view(), name='category_update'),
    path('categories/delete/<uuid:pk>/', HolidaysPackagesCategoryDelete.as_view(), name='category_delete'),

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





]
