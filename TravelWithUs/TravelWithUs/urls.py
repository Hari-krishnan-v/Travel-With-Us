"""
URL configuration for TravelWithUs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('transportation/', include('transportation.urls')),
    path('accommodation/', include('accommodation.urls')),
    path('location/', include('location.urls')),
    # path('budget/', include('budget.urls')),
    # path('itinerary/', include('itinerary.urls')),
    # path('schedule/', include('schedule.urls')),
    # path('payment/', include('payment.urls')),
    # path('attraction/', include('attraction.urls')),
    # path('food/', include('food.urls')),
    # path('dashboard/', include('dashboard.urls')),
    # path('review/', include('review.urls')),
    path('users/trip/', include('trips.urls')),
    path('users/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
