from django import forms
from .models import BoardGame, Participant, Event


class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = '__all__'

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'