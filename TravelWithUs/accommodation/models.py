from django.db import models
from trips.models import  TripPlan

# Create your models here.
class Accommodation(models.Model):
    trip_plan = models.ForeignKey(TripPlan,on_delete=models.CASCADE , related_name='accommodation')
    accommodation_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    total_cost = models.DecimalField(max_digits=10,decimal_places=2)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

