class Grid:
	def __init__(self, string):
		self.grid = [[char for char in row] for row in string.split("\n")]

		self.rows = len(self.grid)
		self.cols = len(self.grid[0])

		self.SOURCE = 'S'
		self.LASER = '|'
		self.SPLITTER = '^'
		self.AIR = '.'

	def get_char(self, x, y):
		if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
			return

		return self.grid[y][x]

	def set_char(self, x, y, char):
		if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
			return

		self.grid[y][x] = char

	def update_char(self, x, y):
		char = self.get_char(x, y)
		char_below = self.get_char(x, y + 1)

		match char:
			case self.SOURCE:
				self.set_char(x, y + 1, self.LASER)
			case self.LASER:
				if char_below == self.SPLITTER:
					self.set_char(x - 1, y + 1, self.LASER)
					self.set_char(x + 1, y + 1, self.LASER)
				elif char_below == self.AIR:
					self.set_char(x, y + 1, self.LASER)

	def update_row(self, row):
		for col in range(self.cols):
			self.update_char(col, row)

	def update(self):
		for row in range(self.rows):
			self.update_row(row)

	def get_laser_count(self):
		count = 0

		for y in range(self.rows):
			for x in range(self.cols):
				if self.get_char(x, y) == self.SPLITTER and self.get_char(x, y - 1) == self.LASER:
					count += 1

		return count

	def display(self):
		for row in self.grid:
			print("".join(row))

input_file = "input.txt"

with open(input_file) as file:
	input_string = file.read()

grid = Grid(input_string)

grid.update()
grid.display()

print(grid.get_laser_count())