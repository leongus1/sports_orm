from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		"All_Baseball_Leagues": League.objects.filter(sport="Baseball"),
		"All_Women_Leagues": League.objects.filter(name__icontains="women"),
		"Any_Type_of_Hockey_Leagues": League.objects.filter(sport__icontains="hockey"),
		"All_Leagues_that_isnt_football": League.objects.exclude(sport="Football"),
		"All_Conference_Leagues": League.objects.filter(name__icontains="conference"),
		"All_Atlantic_Leagues": League.objects.filter(name__icontains="atlantic"), 
		"All_Dallas_Teams": Team.objects.filter(location="Dallas"),
		"All_Raptor_Teams": Team.objects.filter(team_name__icontains="raptor"),
		"All_City_teams": Team.objects.filter(location__icontains="city"),
		"All_T_Teams": Team.objects.filter(team_name__startswith="T"),
		"All_teams_ordered_in_alpha_order_by_city": Team.objects.all().order_by('location'),
		"All_Cooper_last_name_players": Player.objects.filter(last_name = "Cooper"),
		"All_players_named_Joshua": Player.objects.filter(first_name = "Joshua"),
  		"All_Cooper_last_name_players_except_Joshua": Player.objects.filter(last_name = "Cooper").exclude(first_name="Joshua"),
		"Allplayers_names_Alexander_or_Wyatt": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")