from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    user_roll = (
        ('admin','admin'),
        ('client','client')
    )
    user_type = models.CharField(max_length=20, choices=user_roll, default = 'admin')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=260)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()