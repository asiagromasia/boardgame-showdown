from django.test import TestCase
from django.urls import reverse
from .forms import BoardGameForm, ParticipantForm, EventForm
from .models import BoardGame, Participant, Event
from datetime import date

# Create your tests here.

class BoardGameTest(TestCase):
    def test_stringOutput(self):
        game = BoardGame(gamename='Pandemic')
        self.assertEqual(str(game), game.gamename)

    def test_tableName(self):
        self.assertEqual(str(BoardGame._meta.db_table), 'boardgame')

class ParticipantTest(TestCase):
    def test_stringOutput(self):
        participant = Participant(name="Tess")
        self.assertEqual(str(participant), participant.name)

    def test_tableName(self):
        self.assertEqual(str(Participant._meta.db_table), 'participant')

class EventTest(TestCase):
    def test_stringOutput(self):
        event = Event(date=date.today())
        self.assertEqual(str(event), 'Showdown Event on ' + str(event.date))

    def test_tableName(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class TestIndex(TestCase):
    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'showdown/index.html')

class NewBoardGameFormTest(TestCase):
    def test_product_form_is_valid(self):
        form = BoardGameForm(
            data={'gamename': 'Pandemic', 
            'minnumberplayers': 2, 
            'maxnumberplayers': 4, 
            'gameplaylength': 45, 
            'iscooperative': True})
        self.assertTrue(form.is_valid())

    def test_product_form_is_invalid(self):
        # gamename left off
        form = BoardGameForm(
            data={'minnumberplayers': 2, 
            'maxnumberplayers': 4, 
            'gameplaylength': 45, 
            'iscooperative': True})
        self.assertFalse(form.is_valid())

class NewParticipantFormTest(TestCase):
    def test_product_form_is_valid(self):
        form = ParticipantForm(
            data={'name': 'Tess', 
            'score': 42, 
            'bio': "I'm a fuzzy dog, I don't know how to play board games.", 
            'paid': False})
        self.assertTrue(form.is_valid())

    def test_product_form_is_invalid(self):
        # name left off
        form = ParticipantForm(
            data={'score': 42, 
            'bio': "I'm a fuzzy dog, I don't know how to play board games.", 
            'paid': False})
        self.assertFalse(form.is_valid())

class NewEventFormTest(TestCase):
    def test_product_form_is_valid(self):
        form = EventForm(
            data={'date': '2019-03-22',
            'time': '12:00 p.m.', 
            'location': 'Seattle'})
        self.assertTrue(form.is_valid())

    def test_product_form_is_invalid(self):
        # date left off
        form = EventForm(
            data={'time': '12:00 p.m.', 
            'location': 'Seattle'})
        self.assertFalse(form.is_valid())

class GetBoardGamesTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/showdown/boardgames')
        self.assertTrue(200 <= response.status_code)
        self.assertTrue(response.status_code < 400)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('boardgames'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('boardgames'))
        self.assertTemplateUsed(response, 'showdown/boardgames.html')

class GetParticipantsTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/showdown/participants')
        self.assertTrue(200 <= response.status_code)
        self.assertTrue(response.status_code < 400)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('participant'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('participant'))
        self.assertTemplateUsed(response, 'showdown/participants.html')

class GetEventsTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/showdown/event')
        self.assertTrue(200 <= response.status_code)
        self.assertTrue(response.status_code < 400)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('event'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('event'))
        self.assertTemplateUsed(response, 'showdown/event.html')
