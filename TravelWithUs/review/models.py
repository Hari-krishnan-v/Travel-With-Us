from django.db import models
from trips.models import TripPlan
from users.models import User
# Create your models here.
class Review(models.Model):
    trip_plan = models.ForeignKey(TripPlan,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)