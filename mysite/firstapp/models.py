from django.db import models

# Create your models here.

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class sensorData(models.Model):
    datetime = models.DateTimeField(auto_now_add = True )
    temp = models.DecimalField(max_digits=3, decimal_places=2)
    hum = models.DecimalField(max_digits=3, decimal_places=2)
