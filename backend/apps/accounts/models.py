from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.models import TimeStampedModel

from .managers import UserManager


class User(AbstractUser, TimeStampedModel):
    phone_number = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="users/images", null=True, blank=True)
    username = None
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"