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
    path('football/<int:football_id>/', views.football_detail, name='footballdetail'),
    path('basketball/<int:basketball_id>/', views.basketball_detail, name='basketballdetail'),
    path('baseball/<int:baseball_id>/', views.baseball_detail, name='baseballdetail'),
    path('mma/<int:mma_id>/', views.mma_detail, name='mmadetail'),
    path('soccer/<int:soccer_id>/', views.soccer_detail, name='soccerdetail'),
    path('hockey/<int:hockey_id>/', views.hockey_detail, name='hockeydetail'),
]
