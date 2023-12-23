import sys
sys.setrecursionlimit(1000000)

input_file = open('input.txt', 'r')

grid = []

for line in input_file:
	line = line.rstrip('\n')

	grid.append([c for c in line])

def takeStep(x, y, path):
	global grid

	path = path[:]
	path.append((x, y))

	c = grid[y][x]

	to_try = []
	if c == '>':
		to_try = [(x + 1, y)]
	elif c == '<':
		to_try = [(x - 1, y)]
	elif c == 'v':
		to_try = [(x, y + 1)]
	elif c == '^':
		to_try = [(x, y - 1)]
	else:
		to_try = [(x + m[0], y + m[1]) for m in [(0, 1), (1, 0), (0, -1), (-1, 0)]]

	highest = 0
	for n in to_try:
		nx, ny = n

		if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
			continue

		if grid[ny][nx] == '#':
			continue

		if nx == len(grid[0]) - 2 and ny == len(grid) - 1:
			return len(path)

		if (nx, ny) in path:
			continue

		highest = max(highest, takeStep(nx, ny, path))
	return highest

print(takeStep(1, 0, []))