class PaperGrid:
	def __init__(self, string):
		self.grid = [[char for char in row] for row in string.split("\n")]
		self.height = len(self.grid)
		self.width = len(self.grid[0])
	
	def count_neighbors(self, x, y):
		count = 0

		for dy in range(-1, 2):
			for dx in range(-1, 2):
				if dx == 0 and dy == 0:
					continue;

				nx = x + dx
				ny = y + dy

				if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
					continue;

				if self.grid[ny][nx] == "@":
					count += 1

		return count

	def get_accessible_papers(self):
		accessible_papers = []

		for y in range(self.height):
			for x in range(self.width):
				if self.grid[y][x] == ".":
					continue

				if self.count_neighbors(x, y) < 4:
					accessible_papers.append((x, y))

		return accessible_papers

	def remove_papers(self, coords):
		for x, y in coords:
			self.grid[y][x] = "."

	def display(self):
		for y in range(self.height):
			print("".join(self.grid[y]))

input_file = "input.txt"

with open(input_file) as file:
	grid_string = file.read()

grid = PaperGrid(grid_string)

total_paper = 0
accessible_papers = [0]

while accessible_papers:
	accessible_papers = grid.get_accessible_papers()
	num_papers = len(accessible_papers)

	total_paper += num_papers

	grid.remove_papers(accessible_papers)

print(total_paper)