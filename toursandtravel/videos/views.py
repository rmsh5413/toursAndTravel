from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class HolidaysPackagesVideosDelete(generics.DestroyAPIView):
    queryset = HolidaysPackagesVideos.objects.all()
    serializer_class = HolidaysPackagesVideosSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "success": "Videos deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "error": "Failed to delete videos", 
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)