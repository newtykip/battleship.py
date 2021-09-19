from modules.leaderboards import saveScore
from modules.utils import cls, error, rootDir
from structures.Board import Board
import modules.formatting as formatting
import json
import re

def startSingleplayer(name: str):
	cls()
	# Load settings.json
	with open(rootDir + '/settings.json') as f:
		f = json.load(f)
		settings = f.get('singleplayer')
		ships = f.get('general').get('ships')
	# Initiate the game
	board = Board(settings, ships)
	board.score = 11
	saveScore('newtykins', board)
	# torpedos = settings.get('torpedos')
	# # Render the initial board
	# board.render()
	# # While there are still more torpedos to fire
	# while torpedos != 0:
	# 	# Parse the coordinates
	# 	while True:
	# 		try:
	# 			coordinates = input('\n%s, please enter the coordinates you would like to shoot at in an (x,y) format. You have %i torpedos remaining.\n' % (name, torpedos))
	# 			# Remove any brackets from the coordinates
	# 			coordinates = re.sub(r'[\(\)]', '', coordinates)
	# 			coordinates = coordinates.split(',')
	# 			# Parse the co-ordinates
	# 			x = int(coordinates[0])
	# 			y = int(coordinates[1])
	# 			break
	# 		except ValueError:
	# 			cls()
	# 			board.render()
	# 			error('\nPlease enter the coordinates in a valid format this time!')
	# 			continue
	# 		except IndexError:
	# 			cls()
	# 			board.render()
	# 			error('\nPlease enter a pair of two coordinates this time!')
	# 			continue
	# 	# Shoot the shot
	# 	hitResponse = board.shoot(x, y)
	# 	# Render the new board
	# 	cls()
	# 	board.render()
	# 	# 0 = Already hit, 1 = Miss, 2 = Hit, str = Sunk
	# 	if type(hitResponse) is int:
	# 		if hitResponse == 0:
	# 			error("\nYou have already hit (%i,%i) - please select another location!" % (x, y))
	# 		elif hitResponse == 1:
	# 			torpedos -= 1
	# 		elif hitResponse == 2:
	# 			board.score += 1
	# 			torpedos -= 1
	# 	# If a ship has been sunk, announce it
	# 	elif type(hitResponse) is str:
	# 		torpedos -= 1
	# 		board.score += 1
	# 		# Get the name and quantity of the type of the ship
	# 		shipName = board.getShipById(hitResponse).name
	# 		for shipType in ships:
	# 			if shipType.get('name') == shipName:
	# 				shipQuantity = shipType.get('quantity')
	# 		print(formatting.bold(formatting.green("\nCongratulations! You have sunk 1 of %i %ss!" % (shipQuantity, shipName))))
	# gameOver(name, board)

def gameOver(name: str, board: Board):
	cls()
	board.renderResultBoard()
	print(formatting.bold(formatting.green('\nGame over, %s' % (name))))
	print('Your score was: %s' % (formatting.bold(board.score)))
	saveScore(name, board)
