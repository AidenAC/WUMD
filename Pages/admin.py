from django.contrib import admin
from .models import Member, EBoard, Show, Event

# Register your models here.
admin.site.register(Member)
admin.site.register(EBoard)
admin.site.register(Show)
admin.site.register(Event)