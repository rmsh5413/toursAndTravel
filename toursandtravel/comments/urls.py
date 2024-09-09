from django.urls import path
from .views import *

urlpatterns = [

    # HolidaysPackagesComments
    path('comments/create/', HolidaysPackagesCommentsCreate.as_view(), name='comments_create'),
    path('comments/list/', HolidaysPackagesCommentsList.as_view(), name='comments_list'),
    path('comments/detail/<uuid:pk>/', HolidaysPackagesCommentsDetail.as_view(), name='comments_detail'),
    path('comments/delete/<uuid:pk>/', HolidaysPackagesCommentsDelete.as_view(), name='comments_delete'),


    # HolidaysPackagesVideosDelete










]
