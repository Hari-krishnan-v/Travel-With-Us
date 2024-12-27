from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Ensuring that email is unique and being used as the identifier
    email = models.EmailField(max_length=255, unique=True)  # Make email unique
    password = models.CharField(max_length=20)
    is_traveler = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    # Override the default related_name for groups and user_permissions to avoid clashes
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

    # Use the email field as the username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']  # Required fields when creating a user

    # Optionally, you can override the save method if you need any custom logic when saving.
