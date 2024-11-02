from django.contrib.auth.models import AbstractUser
from django.db import models

class workmateUser(AbstractUser):
    email = models.EmailField(unique=True)
    description = models.CharField(max_length=600, default='', blank=True)

    def __str__(self):
        return self.username

# Create your models here.
