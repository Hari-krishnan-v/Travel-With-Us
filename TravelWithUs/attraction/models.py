from django.db import models
from trips.models import  TripPlan
# Create your models here.
class Attraction(models.Model):
    trip_plan = models.ForeignKey(TripPlan, on_delete=models.CASCADE,related_name='attractions')
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    location = models.TextField()
    visit_time = models.DateTimeField(blank=True, null=True)