from django.urls import path
from .views import *

urlpatterns = [
    path('list/', AboutUsList.as_view(), name='aboutus-list'),        
    path('create/', AboutUsCreate.as_view(), name='aboutus-create'),   
    path('detail/<slug:slug>/', AboutUsDetail.as_view(), name='aboutus-detail'),  
    path('update/<uuid:pk>/', AboutUsUpdate.as_view(), name='aboutus-update'),  
    path('homescreen/list/', HomeScreenList.as_view(), name='aboutus-list'),
    path('homescreen/detail/<uuid:pk>/', HomeScreenDetail.as_view(), name='aboutus-detail'),
]