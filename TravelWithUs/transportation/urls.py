# transportation/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightRegisterView, FlightViewSet, BusViewSet, BusRegisterView, TrainRegisterView, TrainViewSet

# Create a router instance
router = DefaultRouter()

# Register the FlightViewSet with the router
router.register(r'flights', FlightViewSet, basename='flight')
router.register(r'buses', BusViewSet , basename='buses')
router.register(r'trains', TrainViewSet, basename='train')

# Define the URL patterns
urlpatterns = [
    path('register-flight/', FlightRegisterView.as_view(), name='register-flight'),
    path('flight-list/', include(router.urls)),
    path('bus-register', BusRegisterView.as_view(), name='bus-register'),
    path('bus-list/', include(router.urls)),
    path('register-train/', TrainRegisterView.as_view(), name='register-train'),
    path('train-list/', include(router.urls)),
]
