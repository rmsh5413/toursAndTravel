from django.urls import path
from .views import *

urlpatterns = [
    path('categories/list/', HolidaysPackagesCategoryList.as_view(), name='categories_list'),
    path('categories/create/', HolidaysPackagesCategoryCreate.as_view(), name='create_category'),
    path('categories/detail/<uuid:pk>/', HolidaysPackagesCategoryDetail.as_view(), name='category_detail'),
    path('categories/update/<uuid:pk>/', HolidaysPackagesCategoryUpdate.as_view(), name='category_update'),
    path('categories/delete/<uuid:pk>/', HolidaysPackagesCategoryDelete.as_view(), name='category_delete'),
]
