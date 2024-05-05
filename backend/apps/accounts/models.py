from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True)
    # date
    birth_date = models.DateField(null=True, blank=True)
    # file
    image = models.ImageField(upload_to="users/images", null=True, blank=True)
    username = None
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()