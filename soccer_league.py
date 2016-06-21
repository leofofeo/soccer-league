
from random import choice
#import total_players collection from players_collection file
from players_collection import all_players

if __name__ == "__main__":
	def find_team(player, available_teams):
		# makes sure that player is assigned to a team that hasn't hit its limit of experienced or
		# inexperienced members
		if player['experience'] == True:
			teams = [team for team in available_teams if team['experienced_members'] < 3]
			team = choice(teams)
		elif player['experience'] == False:
			teams = [team for team in available_teams if team['inexperienced_members'] < 3]
			team = choice(teams)
		return team


	def assign_member(player, teams):
		team = find_team(player, teams) # returns next available team that suits player's experience
		team['members'].append(player) 
		# give the player keys of 'team' and 'practice time' their appropriate values
		player['team'] = team['name']
		player['practice_time'] = team['practice']
		# updates capcity of team in question as necessary to account for new member
		if player['experience'] == True:
			team['experienced_members'] += 1
		elif player['experience'] == False:
			team['inexperienced_members'] += 1
		if len(team['members']) == 6:
			team['full'] = True
			teams.remove(team)

	def write_letter(player):
		# formats salutation appropriately based on number of guardians in question
		if player['guardian_2'] == '':
			salutation = "Dear {},\n".format(player['guardian_1'])
		else:
			salutation = "Dear {} and {},\n".format(player['guardian_1'], player['guardian_2'])
		body = "\nThis is a letter to inform you that {} has been assigned to the {}. Congratulations! The first team practice is on {}. See you then!".format(player['name'], player['team'], player['practice_time'])
		#updates player 'letter' key with letter that will be sent out to guardians
		player['letter'] = salutation + body 

	#create teams in league with all the necessary information
	sharks = {
		'name' : 'Sharks',
		'members' : [],
		'max' : 6,
		'experienced_members' : 0,
		'inexperienced_members' : 0,
		'average_height' : 0, #average height is in here for future updates when I take height into account
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

	LEAGUE = [sharks, dragons, raptors] # all teams in league
	available_teams = [sharks, dragons, raptors] # list gets amended in assign_member() function when a team hits capacity

	# assign player to a team, and write the letter to guardian based on team assignment info
	for player in all_players:
		assign_member(player, available_teams)
		write_letter(player)

	# print player['letter'] value to file
	for player in all_players:
		# I chose to keep player name as one string, so space needs to be replaced with underscore
		filename = player['name'].lower().replace(" ", "_") + ".txt"
		with open(filename, "w") as txt_file:
			txt_file.write(player['letter'])
