from django.db import models

# Create your models here.
class Member (models.Model):
    name = models.CharField('Member Name', max_length=30)
    memberNumber = models.IntegerField(primary_key=True)
    classLevel = models.CharField('Class', max_length=10)

    def __str__(self):
        return self.name
    
class EBoard (models.Model):
    position = models.CharField('Postion', max_length=20, primary_key=True)
    member = models.ForeignKey(Member, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.position
    
class Show (models.Model):
    name = models.CharField('Show Name', max_length=50, primary_key=True)
    host = models.ForeignKey(Member, blank=True, null=True, on_delete=models.CASCADE)
    day = models.CharField('Day on Air', max_length=10, null=True)
    time = models.TimeField('Air Time', null=True)

    def __str__(self):
        return self.name

class Event (models.Model):
    name = models.CharField('Event Name', max_length=50)
    location = models.CharField('Location', max_length=100)
    date = models.DateField('Event Date', primary_key=True)
    time = models.TimeField('Start Time')

    def __str__(self):
        return self.name