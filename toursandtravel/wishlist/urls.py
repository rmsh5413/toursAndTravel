from django.urls import path
from .views  import *


urlpatterns = [
    path('wishlist/create/', WishlistCreate.as_view(), name='wishlist-create'),
    path('wishlist/list/', WishlistList.as_view(), name='wishlist-list'),
    path('wishlist/detail/<uuid:pk>/', WishlistDetail.as_view(), name='wishlist-detail'),
    path('wishlist/update/<uuid:pk>/', WishlistUpdate.as_view(), name='wishlist-update'),
    path('wishlist/delete/<uuid:pk>/', WishlistDelete.as_view(), name='wishlist-delete'),

]