from django.db import models

# Create your models here.

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class sensorData(models.Model):
    datetime = models.DateTimeField(auto_now_add = True )
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    hum = models.DecimalField(max_digits=5, decimal_places=2)

class lightData(models.Model):
    datetime = models.DateTimeField(auto_now_add = True )
    brightness = models.IntegerField(default=-999)

class myTodo(models.Model):
    addedDate = models.DateTimeField(auto_now_add = True )
    description = models.TextField()
    dueDate = models.DateTimeField()
    completed = models.BooleanField(default=False)