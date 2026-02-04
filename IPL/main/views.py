from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def teamForm(request):
    if request.method=='POST':
        create_form=addTeam(request.POST)
        if create_form.is_valid():
            team=create_form.save(commit=False)
            team.save()
            return redirect('display_teams')
    else:
        create_form=addTeam()
    return render(request,'Form.html',{'form':create_form})

def display_teams(request):
    teams=Teams.objects.all()
    return render(request,'team_cards.html',{'teams':teams})

def diplay_team_players(request,id):
    team=Teams.objects.get(team_id=id)
    teamPlayers=team.players.all()
    return render(request,'players.html',{'team':team,'players':teamPlayers})
    




def display_Team(request,id):
    team=Teams.objects.get(team_id=id)
    return render(request,'display_team.html',{'team':team})



#Players
def playerForm(request):
    if request.method=='POST':
        create_form=addPlayer(request.POST)
        if create_form.is_valid():
            player=create_form.save(commit=False)
            player.save()
            return redirect('display_players')
    else:
        create_form=addPlayer()
    return render(request,'Form.html',{'form':create_form})

def display_players(request):
    player=players.objects.all()
    return render(request,'players.html',{'players':player})

def display_allrounders(request):
    allrounder=players.objects.filter(player_type='allrounder')
    return render(request,'players.html',{'players':allrounder})

def display_batsmen(request):
    allrounder=players.objects.filter(player_type='batsmen')
    return render(request,'players.html',{'players':allrounder})

def display_bowlers(request):
    allrounder=players.objects.filter(player_type='bowler')
    return render(request,'players.html',{'players':allrounder})

def search_player(request):
    query=request.GET.get('q')
    results=[]
    if query:
        results=players.objects.filter(name__icontains=query)
    return render(request,'players.html',{'players':results})
        

def delete_player(request,id):
    player=players.objects.get(player_id=id)
    team_name=player.team
    teamid=Teams.objects.get(name=team_name).team_id
   
    player.delete()

    return redirect('display_team_players',teamid)

def update_player(request, id):
    player = players.objects.get(player_id=id)

    if request.method == 'POST':
        form = addPlayer(request.POST,instance=player)
        print("Is form.instance the same?", form.instance == player)
        print("Form.instance.pk:", form.instance.pk)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.player_id = player.player_id  # Force re-assign primary key
            obj.save()
            return redirect('display_players')
    else:
        form = addPlayer(instance=player)

    return render(request, 'updateForm.html', {'form': form})


# def update_player(request, id):
#     player = players.objects.get(player_id=id)

#     if request.method == 'POST':
#         form = addPlayer(request.POST, instance=player)  # handle submitted data
#         if form.is_valid():
#             print("Form instance pk:", form.instance.pk)  # Should be the player's existing ID
#             form.save()
#             return redirect('diplay_players')
#     else:
#         form = addPlayer(instance=player)  # ✅ pre-fills form with existing data

#     return render(request, 'updateForm.html', {'form': form})

# MATCHES

def matchForm(request):
    if request.method=='POST':
        create_form=addMatch(request.POST)
        if create_form.is_valid():
            player=create_form.save(commit=False)
            player.save()
            return redirect('matches')
    else:
        create_form=addMatch()
    return render(request,'Form.html',{'form':create_form})

def matches(request):
    matches=Matches.objects.all()
    return render(request,'matches.html',{'matches':matches})