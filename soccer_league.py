
from random import choice
from collections import defaultdict
#import total_players collection from players_collection file
from players_collection import all_players

def find_team(player, available_teams):
	return choice(available_teams)
 
def assign_member(player, teams):
	team = find_team(player, teams)
	#import pdb; pdb.set_trace()
	team['members'].append(player)
	player['team'] = team['name']
	if player['experience'] == True:
		team['experienced_members'] += 1
	if len(team['members']) == 6:
		team['full'] = True
		teams.remove(team)

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

LEAGUE = [sharks, dragons, raptors]
available_teams = [sharks, dragons, raptors]

for player in all_players:
	assign_member(player, available_teams)

for team in LEAGUE:
	print("\nTeam name: {}".format(team['name']))
	print("Experienced members: {}".format(team['experienced_members']))
	print("Roster:")
	for index, player in enumerate(team['members']):
		print("{}. {}".format(index + 1, player['name']))
