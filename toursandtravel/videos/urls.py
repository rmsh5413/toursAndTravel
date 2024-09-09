from django.urls import path
from .views import *

urlpatterns = [

   

    # HolidaysPackagesVideosDelete
    path('videos/delete/<uuid:pk>/', HolidaysPackagesVideosDelete.as_view(), name='videos_delete'),










]
