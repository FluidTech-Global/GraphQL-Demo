from django.contrib.auth.models import AbstractUser # Enables us to override the built-in Django user model
from django.db import models


class User(AbstractUser):
    """
    Our custom user model
    """

    public_id = models.CharField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "email"
    ]


    class Meta:
        ordering = [
            "first_name"
        ]
        verbose_name = "User"
        verbose_name_plural = "Users"
