
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet,HotelRegistrationView

router = DefaultRouter()


router.register(r'hotels', HotelViewSet, basename='hotels')

urlpatterns = [
    path('hotelRegistration/', HotelRegistrationView.as_view(), name='hotelRegistration'),
    path('hotel-list/', include(router.urls)),
]