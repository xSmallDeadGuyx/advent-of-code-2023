input_file = open('input.txt', 'r')

grid = []

start = ()

for line in input_file:
	line = line.rstrip('\n')

	row = []
	for c in line:
		connections = []
		if c == 'S':
			start = (len(row), len(grid))
		else:
			if c in '|JL':
				connections.append((0, -1))
			if c in '-J7':
				connections.append((-1, 0))
			if c in '|7F':
				connections.append((0, 1))
			if c in '-LF':
				connections.append((1, 0))
		row.append(connections)
	grid.append(row)

def addMove(coord, move):
	return (coord[0] + move[0], coord[1] + move[1])

def getGrid(coord):
	global grid
	return grid[coord[1]][coord[0]]

current = []

for move in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
	coord = addMove(start, move)
	for connection in getGrid(coord):
		if addMove(coord, connection) == start:
			current.append(coord)
			break

prev = [start]

steps = 1
while True:
	connected = []
	for c in current:
		for m in getGrid(c):
			n = addMove(c, m)
			if n not in current and n not in prev:
				connected.append(n)

	if len(connected) == 0:
		# No steps remaining
		break

	steps += 1

	if len(connected) == 1:
		# Both paths lead to same bit
		break

	prev = current
	current = connected

print(steps)
