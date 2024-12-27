from django.urls import path
from .views import trip_add,trip_list
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('newTrip/', trip_add, name='newTrip'),
    path('showAllTrip/', trip_list, name='showAllTrip'),

    ]