from Board import Board
import os
import json
import re

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

# Load settings.json
with open(os.path.dirname(os.path.realpath(__file__)) + '/settings.json') as f:
	settings = json.load(f)

board = Board(8, settings.get('ships'))
torpedos = settings.get('torpedos')
score = 0

# Ready the board and render it
board.spawnShips()
board.render()

while torpedos != 0:
	while True:
		try:
			coordinates = input('\nPlease enter the coordinates you would like to shoot at in an (x,y) format. You have %i torpedos remaining.\n' % (torpedos))
			# Remove any brackets
			coordinates = re.sub(r'[\(\)]', '', coordinates)
			coordinates = coordinates.split(',')
			# Parse the co-ordinates
			x = int(coordinates[0])
			y = int(coordinates[1])
			break
		except ValueError:
			print('Please enter the coordinates in a valid format!\n')
			continue
	isHit = board.shoot(x, y)
	cls()
	board.render()
	if isHit == 0:
		print("\nYou have already hit (%i,%i) - please select another location!" % (x, y))
	elif isHit == 1:
		torpedos -= 1
	elif isHit == 2:
		score += 1
		torpedos -= 1

print("""
Game Over!

Your score was: %i
""" % (score))
board.renderResultBoard()
