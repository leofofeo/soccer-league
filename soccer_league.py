
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
	player['practice_time'] = team['practice']
	if player['experience'] == True:
		team['experienced_members'] += 1
	elif player['experience'] == False:
		team['inexperienced_members'] += 1
	if len(team['members']) == 6:
		team['full'] = True
		teams.remove(team)

def write_letter(player):
	if player['guardian_2'] == '':
		salutation = "Dear {},\n".format(player['guardian_1'])
	else:
		salutation = "Dear {} and {},\n".format(player['guardian_1'], player['guardian_2'])
	body = "\nThis is a letter to inform you that {} has been assigned to the {}. Congratulations! The first team practice is on {}. See you then!".format(player['name'], player['team'], player['practice_time'])
	player['letter'] = salutation + body


sharks = {
	'name' : 'Sharks',
	'members' : [],
	'max' : 6,
	'experienced_members' : 0,
	'inexperienced_members' : 0,
	'average_height' : 0,
	'practice' : 'March 17th, @ 3pm',
	'full' : False
}

dragons = {
	'name' : 'Dragons',
	'members' : [],
	'max' : 6,
	'experienced_members' : 0,
	'inexperienced_members' : 0,
	'average_height' : 0,
	'practice' : 'March 17th, @ 1pm',
	'full' : False
}

raptors = {
	'name' : 'Dragons',
	'members' : [],
	'max' : 6,
	'experienced_members' : 0,
	'inexperienced_members' : 0,
	'average_height' : 0,
	'practice' : 'March 18th, @ 1pm',
	'full' : False
}

LEAGUE = [sharks, dragons, raptors]
available_teams = [sharks, dragons, raptors]

for player in all_players:
	assign_member(player, available_teams)
	write_letter(player)

for player in all_players:
	filename = player['name'].lower().replace(" ", "_") + ".txt"
	with open(filename, "w") as txt_file:
		txt_file.write(player['letter'])