from django.urls import path
from . import views 


urlpatterns=[
    path('', views.index, name='index'),
    path('boardgames/', views.boardgames, name='boardgames'),
    path('gamedetails/<int:id>', views.gamedetail, name='gamedetails'),
    path('participants/', views.participant, name ='participant'),
    path('participantdetails/<int:id>', views.participantdetail, name='participantdetail'),
    path('event/', views.event, name ='event'),
    path('eventdetails/<int:id>', views.eventdetail, name='eventdetail'),
]