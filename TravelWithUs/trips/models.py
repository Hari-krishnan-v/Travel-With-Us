# trips

from django.db import models
from users.models import User

class TripPlan(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE,related_name='trip_plans')
    destination = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10,decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)