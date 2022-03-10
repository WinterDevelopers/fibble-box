from django.db import models

# Create your models here.

class Event(models.Model):
    Event_name = models.CharField(max_length=100)


