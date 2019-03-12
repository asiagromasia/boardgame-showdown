from django.contrib import admin
from .models import BoardGame, Participant, Event

# Register your models here.
admin.site.register(BoardGame)
admin.site.register(Participant)
admin.site.register(Event)
