from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telefone = models.CharField(max_length=200)
    REQUIRED_FIELDS = ['telefone']

