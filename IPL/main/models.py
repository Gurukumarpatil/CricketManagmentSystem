from django.db import models

teams=[
    ('rcb','RCB'),
    ('csk','CSK'),
    ('rr','RR'),
       ]

class Teams(models.Model):
    # player=models.ForeignKey(players , on_delete=models.CASCADE,related_name='team')
    team_id=models.CharField(primary_key=True)
    name=models.CharField(unique=True)
    home_ground=models.CharField()

    def __str__(self):
        return self.name


class Matches(models.Model):
    match_id=models.CharField(primary_key=True)
    team1=models.ForeignKey(Teams,  on_delete=models.CASCADE, related_name='team1')
    team2=models.ForeignKey(Teams,  on_delete=models.CASCADE, related_name='team2')
    date=models.DateField()
    venue=models.CharField()

    
class players(models.Model):
    
    types=[('allrounder','All Rounder'),
           ('batsmen','Batsmen'),
           ('bowler','Bowelr'),
           ]
    bowling_type=[
        ('LHS','left handed spinner'),
        ('RHS','right handed spinner'),
        ('LHP','left handed pacer'),
        ('RHP', 'right handed pacer'),
    ]
    batting_type=[
        ('RH','Right hand batsman'),
        ('LH','Left hand batsman'),
    ]
    player_id=models.AutoField(primary_key=True)
    name=models.CharField()
    team=models.ForeignKey(Teams,  on_delete=models.CASCADE, related_name='players')
    player_type=models.CharField(choices=types,default='unknown')
    bowling_role=models.CharField(choices=bowling_type, default='unknown')
    batting_role=models.CharField(choices=batting_type,default='unknown')
    is_wk=models.BooleanField(default=True)

    def __str__(self):
        return self.name




