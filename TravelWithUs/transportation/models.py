from django.db import models
from trips.models import  TripPlan
# Create your models here.
class Transportation(models.Model):
    transportation_id = models.AutoField(primary_key=True)
    trip_plan = models.ForeignKey(TripPlan,on_delete=models.CASCADE , related_name='transportation')
    mode = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    departure_location = models.CharField(max_length=255)
    arrival_location = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    airline = models.CharField(max_length=100)
    flightImageUrl = models.URLField(blank=True, null=True)
    flight_number = models.CharField(max_length=10)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    layover_time = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.airline

class Bus(models.Model):
    bus_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100)
    busImageUrl = models.URLField(blank=True, null=True)
    bus_number = models.CharField(max_length=10)
    departure_location = models.CharField(max_length=100)
    arrival_location = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    layover_time = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.company

class Train(models.Model):
    train_id = models.AutoField(primary_key=True)
    train_name = models.CharField(max_length=200)
    trainImageUrl = models.URLField(blank=True, null=True)
    departure_location = models.CharField(max_length=100)
    arrival_location = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    layover_time = models.DurationField(blank=True, null=True)


    def __str__(self):
        return self.train_name