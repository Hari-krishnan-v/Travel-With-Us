# serializers.py
from rest_framework import serializers
from .models import Flight, Bus, Train


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            'airline',
            'flight_number',
            'departure_airport',
            'arrival_airport',
            'departure_time',
            'arrival_time',
            'layover_time'
        ]

    def validate_transportation(self, value):
        """
        Ensures that a valid transportation object exists.
        """
        if not Flight.objects.filter(flight_number=value).exists():
            raise serializers.ValidationError("Transportation with this ID does not exist.")
        return value

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'