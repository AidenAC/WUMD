from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('shows', views.shows, name="shows"),
    path('events', views.events, name="events"),
    path('event/<str:event_pk>', views.eventInfo, name="event-info")
]