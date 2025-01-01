from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Hotel
from .serializers import HotelSerializer


# Create your views here.

class HotelRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Hotel.objects.all()
    serializer_class = HotelSerializer

    def update(self, request, *args, **kwargs):
        # Custom PUT method (full update)
        instance = self.get_object()  # Get the current Hotel instance
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Partial update (PATCH)
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        # Custom PATCH method (partial update)
        instance = self.get_object()  # Get the current Hotel instance
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Partial update (PATCH)
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Custom DELETE method
        instance = self.get_object()  # Get the current Hotel instance
        serializer = self.get_serializer(instance)
        serializer.delete()  # Delete the instance
        return Response(status=status.HTTP_204_NO_CONTENT)
