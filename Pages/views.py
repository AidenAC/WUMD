from django.shortcuts import render
from .models import Event

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def events(request):
    eventList = Event.objects.all()
    return render(request, 'events.html', {'eventList': eventList})