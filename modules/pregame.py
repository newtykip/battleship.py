from modules.utils import cls, BANNER, exitGame, hasPlayed
from modules.singleplayer import startSingleplayer
from modules.leaderboards import renderLeaderboard
import modules.formatting as formatting
import time

def onboarding():
	cls()
	playerName = input(formatting.bold(formatting.green("""
Hello, I'm Battleship.py! What is your name?\n
""")))
	if hasPlayed(playerName):
		greeting = 'Welcome back'
	else:
		greeting = 'It\'s nice to meet you'
	print(formatting.red("""
%s, %s! Enjoy the game! <3
	""") % (greeting, playerName))
	time.sleep(2)
	cls()
	return playerName

def mainMenu(name: str):
	error = False
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
				startSingleplayer(name)
			elif choice == 2:
				viewLeaderboards(name)
			elif choice == 3:
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
