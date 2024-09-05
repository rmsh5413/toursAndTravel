from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HolidaysPackagesCategoryList(generics.ListAPIView):
    queryset = HolidaysPackagesCategory.objects.all()
    serializer_class = HolidaysPackagesCategorySerializer


    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "success": "List retrieved successfully", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "Failed to retrieve list", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class HolidaysPackagesCategoryCreate(generics.CreateAPIView):
    queryset = HolidaysPackagesCategory.objects.all()
    serializer_class = HolidaysPackagesCategorySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                "success": "Category created successfully", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "error": "Failed to create category", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        


class HolidaysPackagesCategoryDetail(generics.RetrieveAPIView):
    queryset = HolidaysPackagesCategory.objects.all()
    serializer_class = HolidaysPackagesCategorySerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                "success": "Category retrieved successfully", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "Failed to retrieve category", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        


class HolidaysPackagesCategoryUpdate(generics.UpdateAPIView):
    queryset = HolidaysPackagesCategory.objects.all()
    serializer_class = HolidaysPackagesCategorySerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                "success": "Category updated successfully", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "Failed to update category", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        

class HolidaysPackagesCategoryDelete(generics.DestroyAPIView):
    queryset = HolidaysPackagesCategory.objects.all()
    serializer_class = HolidaysPackagesCategorySerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "success": "Category deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "error": "Failed to delete category", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)