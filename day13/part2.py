input_file = open('input.txt', 'r')

def compareRows(a, b):
	diff = 0
	for x in zip(a, b):
		if x[0] != x[1]:
			diff += 1
	return diff

def findOffByOneReflection(grid):
	for i in range(0, len(grid) - 1):
		total_diff = compareRows(grid[i], grid[i + 1])
		j = 1

		# While possible off by one reflection, keep going
		while total_diff <= 1 and i - j >= 0 and i + j + 1 < len(grid):
			total_diff += compareRows(grid[i - j], grid[i + j + 1])
			j += 1
		if total_diff == 1:
			return i + 1
	return -1

def findEitherReflection():
	global total, normal_grid, rotated_grid
	horiz_reflect = findOffByOneReflection(normal_grid)
	if horiz_reflect > 0:
		total += horiz_reflect * 100
	else:
		vert_reflect = findOffByOneReflection(rotated_grid)
		total += vert_reflect


total = 0
normal_grid = []
rotated_grid = []
for line in input_file:
	line = line.rstrip('\n')

	if '.' not in line and '#' not in line:
		# End of grid
		findEitherReflection()
		normal_grid = []
		rotated_grid = []
	else:
		if len(rotated_grid) == 0:
			rotated_grid = [c for c in line]
		else:
			for i, c in enumerate(line):
				rotated_grid[i] += c
		normal_grid.append(line)

# Handle the last grid if no empty line
findEitherReflection()

print(total)