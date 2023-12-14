input_file = open('input.txt', 'r')

grid = []

for line in input_file:
	line = line.rstrip('\n')
	grid.append([2 if c == '#' else (1 if c == 'O' else 0) for c in line])

def addMoves(a, b):
	return (a[0] + b[0], a[1] + b[1])

def isEmpty(coord):
	if coord[0] < 0 or coord[1] < 0:
		return False
	if coord[0] >= len(grid[0]) or coord[1] >= len(grid):
		return False
	return grid[coord[1]][coord[0]] == 0

def shiftRocks(dir):
	global grid
	max_x = len(grid[0]) - 1
	max_y = len(grid) - 1
	start_x, end_x, step_x = (max_x, -1, -1) if dir[0] == 1 else (0, max_x + 1, 1)
	start_y, end_y, step_y = (max_y, -1, -1) if dir[1] == 1 else (0, max_y + 1, 1)

	for y in range(start_y, end_y, step_y):
		for x in range(start_x, end_x, step_x):
			if grid[y][x] == 1:
				coord = (x, y)
				next_coord = addMoves(coord, dir)
				while isEmpty(next_coord):
					coord = next_coord
					next_coord = addMoves(next_coord, dir)

				grid[y][x] = 0
				grid[coord[1]][coord[0]] = 1

def gridStr():
	global grid
	return '\n'.join(''.join(str(x) for x in row) for row in grid)

prev_grids = [gridStr()]
for i in range(1000000000):
	shiftRocks((0, -1))
	shiftRocks((-1, 0))
	shiftRocks((0, 1))
	shiftRocks((1, 0))
	new_grid = gridStr()
	try:
		# See if we've encountered this exact grid before, if not will raise ValueError and continue shifting
		cycle_start = prev_grids.index(new_grid)

		# We have, so we know there is a perfect cycle from cycle_start to the current iteration
		cycle_len = len(prev_grids) - cycle_start

		# Find out where we will be within that cycle after 1000000000 iterations
		final_index = (1000000000 - cycle_start) % cycle_len + cycle_start

		# Do the rock maths
		total = 0
		split_grid = prev_grids[final_index].split('\n')
		for y, row in enumerate(split_grid):
			total += (len(split_grid) - y) * row.count('1')

		print(total)
		break
	except ValueError:
		# Not found cycle yet, continue
		prev_grids.append(new_grid)