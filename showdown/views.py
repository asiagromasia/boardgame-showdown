from django.shortcuts import render, get_object_or_404
from .models import BoardGame, Participant, Event 
from .forms import BoardGameForm, ParticipantForm, EventForm
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

#form views

def newGame (request):
    form = BoardGameForm
    if request.method=='POST':
        form=BoardGameForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=BoardGameForm()
    else: 
        form=BoardGameForm()
    return render(request, 'showdown/newgame.html', {'form': form})


def newParticipant (request):
    form = ParticipantForm
    if request.method=='POST':
        form=ParticipantForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ParticipantForm()
    else: 
        form=ParticipantForm()
    return render(request, 'showdown/newparticipant.html', {'form': form})

def newEvent (request):
    form = EventForm
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
    else: 
        form=EventForm()
    return render(request, 'showdown/newevent.html', {'form': form})
