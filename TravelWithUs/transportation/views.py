# views.py
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Flight, Bus, Train
from .serializers import FlightSerializer, BusSerializer, TrainSerializer
from rest_framework import viewsets

class FlightRegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # Validate and create the flight data
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the flight record
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlightViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Flight.objects.all()
    serializer_class = FlightSerializer

    def update(self, request, *args, **kwargs):
        # Custom PUT method (full update)
        instance = self.get_object()  # Get the current Flight instance
        serializer = self.get_serializer(instance, data=request.data, partial=False)  # Full update (PUT)
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        # Custom PATCH method (partial update)
        instance = self.get_object()  # Get the current Flight instance
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Partial update (PATCH)
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Custom DELETE method
        instance = self.get_object()  # Get the current Flight instance
        instance.delete()  # Delete the instance
        return Response(status=status.HTTP_204_NO_CONTENT)




class BusRegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Bus.objects.all()
    serializer_class = BusSerializer

    def update(self, request, *args, **kwargs):
        # Custom PUT method (full update)
        instance = self.get_object()  # Get the current Bus instance
        serializer = self.get_serializer(instance, data=request.data, partial=False)  # Full update (PUT)
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        # Custom PATCH method (partial update)
        instance = self.get_object()  # Get the current Bus instance
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Partial update (PATCH)
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Custom DELETE method
        instance = self.get_object()  # Get the current Bus instance
        instance.delete()  # Delete the instance
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrainRegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = TrainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the current Train instance
        serializer = TrainSerializer(instance, data=request.data, partial=True)  # partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrainViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Train.objects.all()
    serializer_class = TrainSerializer

    def update(self, request, *args, **kwargs):
        # Custom PUT method (full update)
        instance = self.get_object()  # Get the current Train instance
        serializer = self.get_serializer(instance, data=request.data, partial=False)  # Full update (PUT)
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        # Custom PATCH method (partial update)
        instance = self.get_object()  # Get the current Train instance
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Partial update (PATCH)
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Custom DELETE method
        instance = self.get_object()  # Get the current Train instance
        instance.delete()  # Delete the instance
        return Response(status=status.HTTP_204_NO_CONTENT)
