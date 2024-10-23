from django.db import models


# Create your models here.
class Button(models.Model):
    link = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
