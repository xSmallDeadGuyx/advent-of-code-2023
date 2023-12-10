input_file = open('input.txt', 'r')

cardinals = [(-1, 0), (0, -1), (1, 0), (0, 1)]
corners = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

grid = []
raw_grid = []

start = ()

for line in input_file:
	line = line.rstrip('\n')

	row = []
	raw_row = []
	for c in line:
		raw_row.append(c)
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
	raw_grid.append(raw_row)

searched = [[False for x in row] for row in grid]

def addMove(coord, move):
	return (coord[0] + move[0], coord[1] + move[1])

def getGrid(coord):
	global grid
	return grid[coord[1]][coord[0]]

def hasSearched(coord):
	global searched
	return searched[coord[1]][coord[0]]

def setSearched(coord):
	global searched
	searched[coord[1]][coord[0]] = True

current = []

setSearched(start)

to_search = ()

first = True
for move in cardinals:
	coord = addMove(start, move)
	for connection in getGrid(coord):
		if addMove(coord, connection) == start:
			current.append(coord)

			# Store the first valid move we come across as our initial search direction when checking inside/outside.
			if first:
				to_search = coord
				first = False
			break

while True:
	connected = []
	for c in current:
		setSearched(c)
		for m in getGrid(c):
			n = addMove(c, m)
			if not hasSearched(n):
				connected.append(n)

	if len(connected) <= 1:
		for c in connected:
			setSearched(c)
		# Done
		break

	current = connected

def getOpposite(direction):
	return (-direction[0], -direction[1])

def validCoord(coord):
	if coord[0] < 0 or coord[1] < 0:
		return False
	if coord[1] >= len(grid) or coord[0] >= len(grid[coord[1]]):
		return False
	return True

def floodFill(coord, filled_list):
	global searched
	# Flood fill from a coord, return -1 if touches the outside or total squares filled otherwise

	if not validCoord(coord):
		return -1

	if hasSearched(coord):
		return 0

	current = [coord]
	setSearched(coord)

	filled_list.append(coord)

	total = 1
	while len(current) > 0:
		c = current.pop(0)
		for m in cardinals:
			n = addMove(c, m)

			if not validCoord(n):
				return -1

			if hasSearched(n):
				continue

			setSearched(n)
			current.append(n)
			filled_list.append(n)
			total += 1
	return total

found_inside_dir = False
stuff_on_inside = 0
stuff_on_outside = 0

stuff_inside = []
stuff_outside = []

# Start by guessing inside direction
move_dir = (to_search[0] - start[0], to_search[1] - start[1])
inside_dir = (-1, 0) if move_dir[0] == 0 else (0, -1)

# Follow the main loop, flood fill everything on both inside and outside until we confirm which direction is inside.
while to_search != start:
	# print(to_search, getGrid(to_search), move_dir, inside_dir)
	for m in getGrid(to_search):
		if m == getOpposite(move_dir):
			# Ignore the way we came
			continue

		moving_to = ()
		if m == inside_dir:
			# Turning towards inside dir
			inside_dir = getOpposite(move_dir)
			move_dir = m
			moving_to = addMove(to_search, move_dir)

			if not found_inside_dir:
				# Flood fill the 5 new outside directions
				to_flood = [getOpposite(move_dir), getOpposite(inside_dir)]
				for nm in corners:
					if nm == addMove(move_dir, inside_dir):
						continue
					to_flood.append(nm)

				for nm in cardinals:
					fill_result = floodFill(addMove(to_search, nm), stuff_outside)
					if fill_result == -1:
						print("Inside guess was correct")
						# Confirmed our guess is correct
						found_inside_dir = True
						break
					elif fill_result > 0:
						stuff_on_outside += fill_result

		elif m == getOpposite(inside_dir):
			# Turning away from inside dir, flood fill the 2 inside directions
			inside_dir = move_dir
			move_dir = m
			moving_to = addMove(to_search, move_dir)

			to_flood = [getOpposite(move_dir), inside_dir]
			for nm in corners:
				if nm == addMove(move_dir, getOpposite(inside_dir)):
					continue
				to_flood.append(nm)

			for nm in to_flood:
				fill_result = floodFill(addMove(to_search, nm), stuff_inside)
				if fill_result == -1:
					if found_inside_dir:
						print("SOMETHING WENT WRONG")
					else:
						print("Inside guess was wrong! Swapping outside and inside", inside_dir, "->", getOpposite(inside_dir), "totals", stuff_on_inside, "->", stuff_on_outside)
						# Our initial guess for inside dir was wrong
						found_inside_dir = True
						inside_dir = getOpposite(inside_dir)
						stuff_on_inside = stuff_on_outside
				elif fill_result > 0:
					stuff_on_inside += fill_result

		elif m == move_dir:
			# Staying same direction, search both inside and outside
			moving_to = addMove(to_search, move_dir)

			outside_dir = getOpposite(inside_dir)
			if not found_inside_dir:
				fill_result = floodFill(addMove(to_search, outside_dir), stuff_outside)
				if fill_result == -1:
					print("Inside guess was correct!")
					# Confirmed out guess is correct
					found_inside_dir = True
				elif fill_result > 0:
					stuff_on_outside += fill_result
			
			fill_result = floodFill(addMove(to_search, inside_dir), stuff_inside)
			if fill_result == -1:
				if found_inside_dir:
					print("SOMETHING WENT WRONG")
				else:
					print("Inside guess was wrong! Swapping outside and inside", inside_dir, "->", getOpposite(inside_dir), "totals", stuff_on_inside, "->", stuff_on_outside)
					# Our initial guess for inside dir was wrong
					found_inside_dir = True
					inside_dir = outside_dir
					stuff_on_inside = stuff_on_outside
			elif fill_result > 0:
				stuff_on_inside += fill_result

		to_search = moving_to
		break

print(stuff_on_inside)
