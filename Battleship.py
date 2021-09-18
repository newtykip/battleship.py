from Board import Board
import os
import json
import re
import csv

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls() # Clear anything that may currently be in the terminal

currentDir = os.path.dirname(os.path.realpath(__file__))
# Load settings.json
with open(currentDir + '/settings.json') as f:
	settings = json.load(f)

board = Board(8, settings)
torpedos = settings.get('torpedos')
score = 0

# Ready the board
board.spawnShips()

# Find out the player's name/alias
playerName = input('Before you play... what would you like to be called?\n')
cls()

# Render the initial board
board.render()

while torpedos != 0:
	while True:
		try:
			coordinates = input('\n%s, please enter the coordinates you would like to shoot at in an (x,y) format. You have %i torpedos remaining.\n' % (playerName, torpedos))
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
	# 0 = Already hit
	# 1 = Miss
	# 2 = Hit
	# str = Sunk
	if isHit == 0:
		print("\nYou have already hit (%i,%i) - please select another location!" % (x, y))
	elif isHit == 1:
		torpedos -= 1
	elif isHit == 2:
		score += 1
		torpedos -= 1
	elif type(isHit) is str:
		score += 1
		torpedos -= 1
		# Get the name and quantity of the type of the ship
		shipName = board.getShipById(isHit).name
		for shipType in settings.get('ships'):
			if shipType.get('name') == shipName:
				shipQuantity = shipType.get('quantity')
		print("\nCongratulations! You have sunk 1 of %i %ss!" % (shipQuantity, shipName))

print("""
Game Over!

Your score was: %i (:
""" % (score))
board.renderResultBoard()

# Save the score to the csv file
with open(currentDir + '/scores.csv', 'w') as f:
	writer = csv.writer(f, delimiter=',')
	writer.writerow([playerName, score])
