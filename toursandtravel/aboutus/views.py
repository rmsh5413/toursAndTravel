from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import*
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AboutUsList(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": "About us retrieved successfully" if serializer.data else "No about us found",
            "data": serializer.data
        }, status=status.HTTP_200_OK if serializer.data else status.HTTP_404_NOT_FOUND)
 


class AboutUsCreate(generics.CreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "About us created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Failed to create about us",
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        




class AboutUsDetail(generics.RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsdetailSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        try:
            aboutus = self.get_object()  
            serializer = self.get_serializer(aboutus) 
            
            return Response({
                "message": "About us retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except AboutUs.DoesNotExist:
            return Response({
                "message": "About us not found",
            }, status=status.HTTP_404_NOT_FOUND)


class AboutUsUpdate(generics.UpdateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "About us updated successfully",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            return Response({
                "message": "Failed to update about us",
                "error": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    

class HomeScreenList(generics.ListAPIView):
    queryset = Homescreen.objects.all()
    serializer_class = HomescreenSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": "Homescreen retrieved successfully" if serializer.data else "No homescreen found",
            "data": serializer.data
        }, status=status.HTTP_200_OK if serializer.data else status.HTTP_404_NOT_FOUND)
    



class HomeScreenDetail(generics.RetrieveAPIView):
    queryset = Homescreen.objects.all()
    serializer_class = HomescreenSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            homescreen = self.get_object()  
            serializer = self.get_serializer(homescreen) 
            
            return Response({
                "message": "Homescreen retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Homescreen.DoesNotExist:
            return Response({
                "message": "Homescreen not found",
            }, status=status.HTTP_404_NOT_FOUND)