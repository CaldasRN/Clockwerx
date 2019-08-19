from django.db import models

# Create your models here.
class Timer(models.Model):
    hour = models.CharField(max_length=2)
    min = models.CharField(max_length=2)
    sec = models.CharField(max_length=2)
