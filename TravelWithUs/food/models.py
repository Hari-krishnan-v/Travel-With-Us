from django.db import models
from trips.models import  TripPlan

# Create your models here.
class Food(models.Model):
    trip_plan = models.ForeignKey(TripPlan,on_delete=models.CASCADE , related_name='food_options')
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    location = models.TextField()
    details = models.TextField(blank=True,null=True)

#     breakfast,lunch,dinner
#     name of restaurant
