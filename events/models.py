from django.contrib.auth.models import User
from django.db import models

# This makes the Event class which incluces a title, location, date, and time. It also has a __str__ function which returns how the function object will be named (eg. Church, 10/28)
class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.title}, {self.date}'
    
# This makes the Registration class which includes a given name and email, along with an event. A similar __str__ function is included which returns the name of the object (eg. James, Church)
class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.event}'
