from Board import Board
import os
import json

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
	coordinates = input('Please enter the coordinates you would like to shoot at in an (x,y) format. You have %i torpedos remaining.\n' % (torpedos)).split(',')
	x = int(coordinates[0])
	y = int(coordinates[1])
	isHit = board.shoot(x, y)
	board.render()
	if isHit == 0:
		print("You have already hit (%i,%i) - please select another location!" % (x, y))
	elif isHit == 1:
		torpedos -= 1
	elif isHit == 2:
		score += 1
		torpedos -= 1
print("Your score was: %i" % (score))
