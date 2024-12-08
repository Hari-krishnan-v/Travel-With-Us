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