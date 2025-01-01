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


from django.db import models


class TouristAttraction(models.Model):
    zone = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    attraction_type = models.CharField(max_length=100,null=True, blank=True)
    establishment_year = models.PositiveIntegerField(null=True, blank=True)
    time_needed_in_hrs = models.FloatField(null=True, blank=True)
    google_review_rating = models.FloatField(null=True, blank=True)
    entrance_fee_in_inr = models.PositiveIntegerField(null=True, blank=True)
    nearest_airport = models.CharField(max_length=255)
    weekly_off = models.CharField(max_length=50, blank=True, null=True)
    significance = models.TextField(null=True, blank=True)
    dslr_allowed = models.BooleanField(default=True)
    google_reviews_in_lakhs = models.FloatField(null=True, blank=True)
    best_time_to_visit = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tourist Attraction"
        verbose_name_plural = "Tourist Attractions"
