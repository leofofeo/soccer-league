
from random import choice
from collections import defaultdict
#import total_players collection from players_collection file
from players_collection import all_players

def find_team(player, available_teams):
	if player['experience'] == True:
		teams = [team for team in available_teams if team['experienced_members'] < 3]
		team = choice(teams)
	elif player['experience'] == False:
		teams = [team for team in available_teams if team['inexperienced_members'] < 3]
		team = choice(teams)
	return team


def assign_member(player, teams):
	team = find_team(player, teams)
	team['members'].append(player)
	player['team'] = team['name']
	if player['experience'] == True:
		team['experienced_members'] += 1
	elif player['experience'] == False:
		team['inexperienced_members'] += 1
	if len(team['members']) == 6:
		team['full'] = True
		teams.remove(team)

sharks = {
	'name' : 'Sharks',
	'members' : [],
	'max' : 6,
	'experienced_members' : 0,
	'inexperienced_members' : 0,
	'average_height' : 0,
	'full' : False
}

dragons = {
	'name' : 'Dragons',
	'members' : [],
	'max' : 6,
	'experienced_members' : 0,
	'inexperienced_members' : 0,
	'average_height' : 0,
	'full' : False
}

raptors = {
	'name' : 'Raptors',
	'members' : [],
	'max' : 6,
	'experienced_members' : 0,
	'inexperienced_members' : 0,
	'average_height' : 0,
	'full' : False
}

LEAGUE = [sharks, dragons, raptors]
available_teams = [sharks, dragons, raptors]

for player in all_players:
	assign_member(player, available_teams)

for team in LEAGUE:
	print("\nTeam name: {}".format(team['name']))
	print("Experienced members: {}".format(team['experienced_members']))
	print("Roster:")
	for index, player in enumerate(team['members']):
		print("{}. {}, experienced? {}".format(index + 1, player['name'], player['experience']))
		print("-Member of the {}".format(player['team']))
