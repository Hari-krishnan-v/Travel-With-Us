from rest_framework import serializers
from .models import TripPlan

class TripPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPlan
        fields = ('user','destination','budget','start_date','end_date','created_at','updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("Start date cannot be later than end date.")
        return data
