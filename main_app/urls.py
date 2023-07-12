from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('football/', views.football_index, name='footballindex'),
    path('basketball/', views.basketball_index, name='basketballindex'),
    path('baseball/', views.baseball_index, name='baseballindex'),
    path('mma/', views.mma_index, name='mmaindex'),
    path('soccer/', views.soccer_index, name='soccerindex'),
    path('hockey/', views.hockey_index, name='hockeyindex'),
]
