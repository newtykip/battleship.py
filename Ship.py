from uuid import uuid4 as uuid
import random

class Ship:
	def __init__(self, name: str, shipSize: int):
		self.id = uuid().__str__()
		self.name = name
		self.size = shipSize
		self.vertical = random.random() > 0.5
		self.spawned = False
		self.hit = False

	# Generate a datapoint that represents the ship and its state
	def generateDatapoint(self):
		return { 'id': self.id, 'shipName': self.name, 'hit': self.hit }

	# Spawn the ship into the grid
	def spawn(self, grid: list[list[dict]], gridSize: int):
		# Keep trying until spawning is successful
		while not self.spawned:
			# Horizontal Spawning
			if not self.vertical:
				# Attempt some base coordinates
				x = random.randint(0, gridSize - 1 - self.size)
				y = random.randint(0, gridSize - 1)
				placement = grid[y][x]
				# Ensure that the coordinates will be valid and not overlap
				while placement.get('id') != None:
					x = random.randint(0, gridSize - 1 - self.size)
					y = random.randint(0, gridSize - 1)
					placement = grid[y][x]
				# Place in the self and register it as spawned
				for i in range(self.size):
					grid[y][x] = self.generateDatapoint()
					grid[y][x + i] = self.generateDatapoint()
				self.spawned = True
			# Vertical spawning
			else:
				# Attempt some base coordinates
				x = random.randint(0, gridSize - 1)
				y = random.randint(0, gridSize - 1 - self.size)
				placement = grid[y][x]
				# Ensure that the coordinates will be valid and not overlap
				while placement.get('id') != None:
					x = random.randint(0, gridSize - 1)
					y = random.randint(0, gridSize - 1 - self.size)
					placement = grid[y][x]
				# Place in the self and register it as spawned
				for i in range(self.size):
					grid[y][x] = self.generateDatapoint()
					grid[y + i][x] = self.generateDatapoint()
				self.spawned = True
