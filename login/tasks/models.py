from django.db import models
from django import forms
from django.forms import ModelChoiceField
from workmates.models import workmateUser

class Tasks(models.Model):
    class Urgency (models.IntegerChoices):
        LV1 = 1, "Level 1"
        LV2 = 2, "Level 2"
        LV3 = 3, "Level 3"
        LV4 = 4, "Level 4"
        LV5 = 5, "Level 5"
    class Categories (models.TextChoices):
        ("TECH", "Tecnologico"),
        ("ADMIN", "Administrativo"),
        ("DEV", "Desarrollo"),
        ("TEAM", "WorkMate Internal")
        ("OTHER", "Otro/No Listado")

    description = models.TextField(max_length = 600, blank=False)
    category = forms.ChoiceField(choices=Categories)
    priority = models.IntegerField(default=Urgency.LV1, choices=Urgency, blank=False)
    notes = models.TextField(max_length = 300, blank=True)

    def __str__(self):
        return self.description, self.category, self.priority, self.notes


class TaskProfile(models.Model):
    class wmusers(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return "{0} {1}".format(obj.first_name,obj.last_name)
        
    listofwm = wmusers(queryset = workmateUser.objects.all())
    def __str__(self):
        return self.listofwm
# Create your models here.