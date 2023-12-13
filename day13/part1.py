input_file = open('input.txt', 'r')

def findReflection(grid):
	for i in range(0, len(grid) - 1):
		if grid[i] == grid[i + 1]:
			# Possible reflection, continue checking
			j = 0
			while True:
				j += 1
				if i - j < 0 or i + j + 1 >= len(grid):
					return i + 1
				if grid[i - j] != grid[i + j + 1]:
					break
	return -1

def findEitherReflection():
	global total, normal_grid, rotated_grid
	horiz_reflect = findReflection(normal_grid)
	if horiz_reflect > 0:
		total += horiz_reflect * 100
	else:
		vert_reflect = findReflection(rotated_grid)
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