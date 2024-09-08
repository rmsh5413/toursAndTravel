from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class WishlistCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response({
                "message": "Wishlist created successfully."
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "message": "Failed to create wishlist.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)



class WishlistList(generics.ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


    def list(self, request, *args, **kwargs):
        try:
            queryset = Wishlist.objects.filter(user=request.user)
            serializer = WishlistSerializer(queryset, many=True)
            return Response({
                "message": "Wishlist retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Failed to retrieve wishlist.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        


class WishlistDetail(generics.RetrieveAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                "message": "Wishlist retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Failed to retrieve wishlist.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class WishlistUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def perform_update(self, serializer):
        try:
            serializer.save(user=self.request.user)
            return Response({
                "message": "Wishlist updated successfully."
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Failed to update wishlist.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        


class WishlistDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def perform_destroy(self, instance):
        try:
            instance.delete()
            return Response({
                "message": "Wishlist deleted successfully."
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "message": "Failed to delete wishlist.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
