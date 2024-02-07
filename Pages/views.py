from django.shortcuts import render
from .models import Show, Event

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def shows(request):
    showList = Show.objects.all()
    return render(request, 'shows.html', {'showList': showList})

def events(request):
    eventList = Event.objects.all()
    return render(request, 'events.html', {'eventList': eventList})

def eventInfo(request, event_pk):
    event = Event.objects.get(pk = event_pk)
    return render(request, 'event-info.html', {'event': event})