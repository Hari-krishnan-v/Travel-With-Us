from rest_framework import serializers
from .models import TripPlan

class TripPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPlan
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
