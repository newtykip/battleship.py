from modules.utils import cls, BANNER, exitGame, rootDir
from modules.singleplayer import startSingleplayer
from modules.leaderboards import renderLeaderboard
import modules.formatting as formatting
import time
import json

def onboarding():
	cls()
	username = input(formatting.bold(formatting.green("""
Hello, I'm Battleship.py! What is your name?\n
""")))
	print(formatting.red("""
It's nice to meet you, %s! Enjoy the game! <3
	""") % (username))
	time.sleep(2)
	cls()
	# Save the username
	with open(rootDir + '/settings.json') as f:
		settings = json.load(f)
	with open(rootDir + '/settings.json', 'w') as f:
		settings['general']['username'] = username
		f.write(json.dumps(settings, indent=2, sort_keys=True))
		f.close()
	return username

def mainMenu():
	cls()
	error = False
	# Load settings.json
	with open(rootDir + '/settings.json') as f:
		f = json.load(f)
		singleplayerSettings = f.get('singleplayer')
		ships = f.get('general').get('ships')
		name = f.get('general').get('username')
	if name == None:
		name = onboarding()
	print(BANNER)
	print("""
%s, please select an option:

1) Singleplayer
2) Leaderboards
3) Exit
	""" % (formatting.bold(name)))
	while True:
		try:
			choice = int(input('Your choice: '))
			if choice == 1:
				startSingleplayer(name, singleplayerSettings, ships)
			elif choice == 2:
				viewLeaderboards(name)
			elif choice == 3:
				cls()
				exitGame(name)
			break
		except ValueError:
			print('Please enter a valid option!')
			error = True
			break
	if error:
		cls()
		mainMenu(name)
		return

def viewLeaderboards(name: str):
	renderLeaderboard(name)
	for i in range(1, 6):
		print('\nReturning to the main menu in %i...' % (5 - i))
		time.sleep(1)
		renderLeaderboard(name)
	mainMenu(name)
