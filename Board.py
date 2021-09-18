from Ship import Ship

class Board:
	def __init__(self, settings: dict):
		self.settings = settings
		self.ships: list[Ship] = []
		self.size = settings.get('boardSize')
		self.score = 0
		# Generate an empty grid to play in
		self.grid: list[list[dict]] = []
		for i in range(self.size):
			row = []
			for j in range(self.size):
				col = { 'id': None, 'name': None, 'hit': False }
				row.append(col)
			self.grid.append(row)
		# Populate self.ships with the JSON data
		for shipData in settings.get('ships'):
			for i in range(shipData.get('quantity')):
				ship = Ship(shipData.get('name'), shipData.get('size'))
				self.ships.append(ship)

	# Spawn all ships populated in self.ships into the grid
	def spawnShips(self):
		for ship in self.ships:
			ship.spawn(self.grid, self.size)

	# Find a ship by its UUID
	def getShipById(self, id: str) -> Ship:
		for ship in self.ships:
			if ship.id == id:
				return ship
	
	# Shoot at a coordinate
	# returns:
	# 0 - Already hit
	# 1 - New hit, miss
	# 2 - New hit, success
	# str - New hit, ship sunk (return is the ship ID)
	def shoot(self, x: int, y: int):
		# i = y, j = x
		for i, row in enumerate(self.grid):
			for j, col in enumerate(row):
				if x == j + 1 and y == i + 1:
					if col.get('hit') != True:
						col['hit'] = True
						if col.get('id') != None:
							# Check if that was the last of the ship to be sunk
							counter = 0
							for row2 in self.grid:
								for col2 in row2:
									if col2.get('id') == col.get('id'):
										for shipType in self.settings.get('ships'):
											if shipType.get('name') == col2.get('name'):
												# Find the size of the ship in column 2
												col2Size = shipType.get('size')
												if col2.get('hit'):
													counter += 1
												# If the ship has died
												if counter == col2Size:
													return col.get('id')
							self.score += 1
							return 2
						else:
							return 1
					else:
						return 0

	# Render the x-axis
	def generateXAxis(self):
		xAxis = ''
		spaces = '   '
		# Ensure that the axis will align with the first column of the grid 
		for i in range(len(str(self.size))):
			xAxis += ' '
		for i in range(self.size):
			# Left center as numbers get too big for their cells (> 9)
			if len(str(i + 1)) > len(str(i)) and len(spaces) > 1:
				spaces = spaces[:len(spaces) - 1]
			# Add a number to the axis
			xAxis += '%s%i' % (spaces, i + 1)
		return xAxis
		
	# Render the board
	def render(self):
		print(self.generateXAxis())
		for rowNumber, row in enumerate(self.grid):
			rowContent = []
			rowNumber = rowNumber + 1
			# Enforce spacing
			spaces = '  '
			if len(str(rowNumber)) < len(str(self.size)):
				spaces += ' '
			# Generate row contents
			for col in row:
				if col.get('hit') and col.get('id') != None:
					rowContent.append('[x]')
				elif col.get('hit'):
					rowContent.append('[o]')
				else:
					rowContent.append('[ ]')
			# Print the row
			print('%i%s%s' % (rowNumber, spaces, ' '.join(rowContent)))

	# Render a version of the board with all of the ships identified
	def renderResultBoard(self):
		print(self.generateXAxis())
		# Render every row, appending a row number
		for rowNumber, row in enumerate(self.grid):
			rowContent = []
			rowNumber = rowNumber + 1
			# Enforce spacing
			spaces = '  '
			if len(str(rowNumber)) < len(str(self.size)):
				spaces += ' '
			# Generate row contents
			for col in row:
				type = col.get('name')
				code = ''
				if type == None:
					code = ' '
				else:
					code = type[0]
				rowContent.append('[%s]' % code)
			# Print the row, and make sure the row number can not be used again
			print('%i%s%s' % (rowNumber, spaces, ' '.join(rowContent)))
