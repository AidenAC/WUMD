from django.db import models

# Create your models here.
class Event (models.Model):
    name = models.CharField('Event Name', max_length=50)
    location = models.CharField('Location', max_length=100)
    date = models.DateField('Event Date', primary_key=True)
    time = models.TimeField('Start Time')

    def __str__(self):
        return self.name