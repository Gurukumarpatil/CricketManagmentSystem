from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Teams)
class Teams(admin.ModelAdmin):
    list_display=('name',)

@admin.register(players)
class Players(admin.ModelAdmin):
    list_display=('player_id','name')

@admin.register(Matches)
class Matches(admin.ModelAdmin):
    list_display=('match_id','team1','team2','date','venue')