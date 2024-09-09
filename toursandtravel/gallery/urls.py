from django.urls import path
from .views import *

urlpatterns = [

      path('gallery/delete/<uuid:pk>/', HolidaysPackagesGalleryDelete.as_view(), name='gallery_delete'),



]
