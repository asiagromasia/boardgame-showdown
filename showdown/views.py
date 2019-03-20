from django.shortcuts import render, get_object_or_404
from .models import BoardGame, Participant, Event 

# Create your views here.
def index(request):
    return render(request, 'showdown/index.html')

def boardgames (request):
    boardgame_list = BoardGame.objects.all()
    return render (request, 'showdown/boardgames.html', {'boardgame_list': boardgame_list})
    
def gamedetail (request, id):
    detail = get_object_or_404(BoardGame, pk=id)
    return render (request, 'showdown/gamedetails.html', {'detail': detail})

def participant (request):
    participant_list = Participant.objects.all()
    return render (request, 'showdown/participants.html', {'participant_list': participant_list})

def participantdetail (request, id):
    detail = get_object_or_404(Participant, pk=id)
    return render (request, 'showdown/participantdetail.html', {'detail': detail})

def event (request):
    event_list = Event.objects.all()
    return render (request, 'showdown/event.html', {'event_list': event_list})

def eventdetail (request, id):
    detail = get_object_or_404(Event, pk=id)
    return render (request, 'showdown/eventdetail.html', {'detail': detail})

