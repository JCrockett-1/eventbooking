from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
