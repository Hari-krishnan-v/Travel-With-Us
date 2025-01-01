from django.urls import path
from .views import get_location

urlpatterns = [
    # Other URL patterns...
    path('locations/', get_location, name='get_location'),
]
