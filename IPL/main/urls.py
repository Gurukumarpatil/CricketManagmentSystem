"""
URL configuration for IPL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('cplayer/',views.playerForm,name='playerForm'),
    path('players/',views.display_players,name='display_players'),
    path('allrounders/',views.display_allrounders,name='display_allrounders'),
    path('batsmen/',views.display_batsmen,name='display_batsmen'),
    path('bowlers/',views.display_bowlers,name='display_bowlers'),
    path('search/',views.search_player,name='search_player'),
    path('updateplayer/<int:id>/',views.update_player,name='update_player'),
    path('deleteplayer/<int:id>/',views.delete_player,name='delete_player'),
    
    path('team/<int:id>/players/',views.diplay_team_players,name='display_team_players'),
    path('cteam/',views.teamForm,name='teamForm'),
    path('teams/',views.display_teams,name='display_teams'),
    
    path('cmatch',views.matchForm,name='matchForm'),
    path('matches/',views.matches,name='matches'),
]