# userdetails
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True , null=True)
    password = models.CharField(max_length=20)
    is_traveler = models.BooleanField(default=True)

#  Override the default related_name for groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_custom',  # Avoids conflict with auth.User.groups
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_set_custom',  # Avoids conflict with auth.User.user_permissions
        blank=True
    )