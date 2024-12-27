from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import TripPlan
from .serializers import TripPlanSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def trip_add(request):
    if request.method == 'POST':  # Corrected typo here
        serializer = TripPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def trip_list(request):
    if request.method == 'GET':
        trips = TripPlan.objects.all()
        serializer = TripPlanSerializer(trips, many=True)
        return JsonResponse(serializer.data, safe=False)
