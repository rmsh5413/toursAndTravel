from rest_framework import generics, status
from rest_framework.response import Response
from .models import Blogs
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.exceptions import NotFound


class BlogCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blogs.objects.all()
    serializer_class = BloggSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "success": True,
                "message": "Blog created successfully.",
                "data": {
                    "id": serializer.instance.id,
                    **serializer.data
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({
                "success": False,
                "message": "Validation failed.",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        

class BlogsDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    lookup_field = 'id' 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                "success": True,
                "message": "Blog deleted successfully."
            },
            status=status.HTTP_204_NO_CONTENT
        )
    

class BlogsDetailAPIView(generics.RetrieveAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    lookup_field = 'slug' 




class BlogsListAPIView(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'

    def get_object(self):
        slug = self.kwargs.get(self.lookup_field)
        try:
            return Blogs.objects.get(slug=slug)
        except Blogs.DoesNotExist:
            raise NotFound(detail="Blog not found", code=404)
        

class BlogsUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blogs.objects.all()
    serializer_class = BloggSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                "success": True,
                "message": "Blog updated successfully.",
                "data": serializer.data
            })
        else:
            return Response({
                "success": False,
                "message": "Validation failed.",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()



class BlogsListView(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    def get(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            response_data = {
                "success": True,
                "message": "Blogs retrieved successfully.",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            return Response({
                "success": False,
                "message": "Failed to retrieve blogs.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            response_data = {
                "success": True,
                "message": "Categories retrieved successfully.",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            return Response({
                "success": False,
                "message": "Failed to retrieve categories.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                "success": True,
                "message": "Category retrieved successfully.",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            return Response({
                "success": False,
                "message": "Failed to retrieve category.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class PopularTagListView(generics.ListAPIView):
    queryset = Tag.objects.filter(blogs__is_popular=True)
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            response_data = {
                "success": True,
                "message": "Popular tags retrieved successfully.",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            return Response({
                "success": False,
                "message": "Failed to retrieve popular tags.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        

class PopularTagDetailView(generics.RetrieveAPIView):
    queryset = Blogs.objects.filter(is_popular=True)
    serializer_class = BlogsSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                "success": True,
                "message": "Popular tag retrieved successfully.",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            return Response({
                "success": False,
                "message": "Failed to retrieve popular tag.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

from rest_framework import filters


class SearchBlogsView(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tags__name', 'category__name']

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            response_data = {
                "success": True,
                "message": "Blogs retrieved successfully.",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            return Response({
                "success": False,
                "message": "Failed to retrieve blogs.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)



class TagDetailView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                "success": True,
                "message": "Tag retrieved successfully.",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            return Response({
                "success": False,
                "message": "Failed to retrieve tag.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)