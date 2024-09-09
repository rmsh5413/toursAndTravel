from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class HolidaysPackagesCommentsCreate(generics.CreateAPIView):
    queryset = HolidaysPackagesComments.objects.all()
    serializer_class = HolidaysPackagesCommentsSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                "success": "Comment created successfully", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "error": "Failed to create comment", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)



class HolidaysPackagesCommentsList(generics.ListAPIView):
    queryset = HolidaysPackagesComments.objects.all()
    serializer_class = HolidaysPackagesCommentsSerializer

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
        

class HolidaysPackagesCommentsDetail(generics.RetrieveAPIView):
    queryset = HolidaysPackagesComments.objects.all()
    serializer_class = HolidaysPackagesCommentsSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                "success": "Comment retrieved successfully", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "Failed to retrieve comment", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        


class HolidaysPackagesCommentsDelete(generics.DestroyAPIView):
    queryset = HolidaysPackagesComments.objects.all()
    serializer_class = HolidaysPackagesCommentsSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "success": "Comment deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "error": "Failed to delete comment", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        