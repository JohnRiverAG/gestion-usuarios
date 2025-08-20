from django.db import models

# Create your models here.

# usuarios/models.py
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True)

