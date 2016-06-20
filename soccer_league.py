
from random import choice
#import total_players collection from players_collection file
from players_collection import all_players

# def find_team(player):
# 	if player['experience'] == True:
# 		team = [x[0] for x in available_teams if x['full'] == False and x['experienced_members'] < 3]
#     else:
#     	team = choice(available_teams)
#     return team

def find_team(player, available_teams):
	for team in available_teams:
		if player['experience'] == True and team['experienced_members'] < 3:
			return team
		else:
			continue
 
def assign_member(player, teams):
	team = find_team(player, teams)
	team['members'].append(player)
	if player['experience'] == True:
		team['experienced_members'] += 1
	if len(team['members']) == 6:
		team['full'] = True
		available_teams.remove(team)

sharks = {
	'name' : 'Sharks',
	'members' : [],
	'max' : 6,
	'experienced_members' : 3,
	'average_height' : 0,
	'full' : False
}

dragons = {
	'name' : 'Dragons',
	'members' : [],
	'max' : 6,
	'experienced_members' : 3,
	'average_height' : 0,
	'full' : False
}

raptors = {
	'name' : 'Raptors',
	'members' : [],
	'max' : 6,
	'experienced_members' : 0,
	'average_height' : 0,
	'full' : False
}

LEAGUE = sharks, dragons, raptors
available_teams = sharks, dragons, raptors

for player in all_players:
	assign_member(player, available_teams)
