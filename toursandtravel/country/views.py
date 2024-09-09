from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CountiresCreateView(generics.CreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                "success": "Country created successfully", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "error": "Failed to create country", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)



class CountriesListView(generics.ListAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer

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
        

class CountriesDetailView(generics.RetrieveAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                "success": "Country retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "Failed to retrieve country",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        


class CountriesUpdateView(generics.UpdateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                "success": "Country updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "Failed to update country",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        


class CountriesDeleteView(generics.DestroyAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "success": "Country deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "error": "Failed to delete country",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        




class CitiesCreateView(generics.CreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                "success": "City created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "error": "Failed to create city",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        


class CitiesListView(generics.ListAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

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
        



class CitiesDetailView(generics.RetrieveAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                "success": "City retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "Failed to retrieve city",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        

class CitiesUpdateView(generics.UpdateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                "success": "City updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "Failed to update city",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        


class CitiesDeleteView(generics.DestroyAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "success": "City deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "error": "Failed to delete city",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        