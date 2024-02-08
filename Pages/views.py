from django.shortcuts import render
from .models import Show, Event

# Create your views here.
def home(request):
    return render(request, 'Pages/home.html', {})

def shows(request):
    showList = Show.objects.all()
    return render(request, 'Pages/shows.html', {'showList': showList})

def events(request):
    eventList = Event.objects.all()
    return render(request, 'Pages/events.html', {'eventList': eventList})

def eventInfo(request, event_pk):
    event = Event.objects.get(pk = event_pk)
    return render(request, 'Pages/event-info.html', {'event': event})