from django.db import models

# Create your models here.

class BoardGame(models.Model):
    gamename = models.CharField(max_length = 255)
    minnumberplayers = models.PositiveSmallIntegerField()
    maxnumberplayers = models.PositiveSmallIntegerField()
    gameplaylength = models.PositiveSmallIntegerField()
    iscooperative = models.BooleanField()

    def __str__(self):
        return self.gamename

    class Meta:
        db_table = 'boardgame'

class Participant(models.Model):
    name = models.CharField(max_length = 255)
    score = models.PositiveSmallIntegerField()
    bio = models.TextField(null = True, blank = True)
    paid = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'participant'

class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length = 255)
    participants = models.ManyToManyField(Participant)
    games = models.ManyToManyField(BoardGame)

    def __str__(self):
        return 'Showdown Event on ' + self.date

    class Meta:
        db_table = 'event'
