from django.urls import path
from .views  import *


urlpatterns = [
    path('create/', WishlistCreate.as_view(), name='wishlist-create'),
    path('list/', WishlistList.as_view(), name='wishlist-list'),
    path('detail/<uuid:pk>/', WishlistDetail.as_view(), name='wishlist-detail'),
    path('update/<uuid:pk>/', WishlistUpdate.as_view(), name='wishlist-update'),
    path('delete/<uuid:pk>/', WishlistDelete.as_view(), name='wishlist-delete'),
]