from django.urls import path
from .views import *

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blogs-create'),
    path('update/<uuid:id>/', BlogsUpdateView.as_view(), name='blogs-update'),
    path('delete/<uuid:id>/', BlogsDeleteAPIView.as_view(), name='blogs-delete'),
    path('detail/<slug:slug>/', BlogsDetailAPIView.as_view(), name='blogs-detail'),
    path('tag/detail/<slug:slug>/', TagDetailView.as_view(), name='tags-detail'),
    path('list/', BlogsListAPIView.as_view(), name='blogs-list'),
    path('is_popular/', BlogsListAPIView.as_view(), name='blogs-is-popular'),
    path('category/list/', CategoryListView.as_view(), name='blogs-category'),
    path('category/detail/<slug:slug>/', CategoryDetailView.as_view(), name='blogs-category-detail'),
    path('populartag/list/', PopularTagListView.as_view(), name='blogs-popular-tag'),
    path('populartag/detail/<uuid:id>/', PopularTagDetailView.as_view(), name='blogs-popular-tag-detail'),
    path('search/', SearchBlogsView.as_view(), name='blogs-search'),
]