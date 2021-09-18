from helper import cls, BANNER, exitGame
from singleplayer import startSingleplayer
from leaderboards import viewLeaderboards
import time

def onboarding():
	cls()
	playerName = input("""
Hello, I'm Battleship.py! What is your name?\n
""")
	print("""
It's nice to meet you, %s! Enjoy the game! <3
	""" % (playerName))
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
	""" % (name))
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
