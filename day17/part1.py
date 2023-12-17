input_file = open('input.txt', 'r')

grid = []
prev = []

for line in input_file:
	line = line.rstrip('\n')

	grid.append([int(c) for c in line])
	prev.append([(-1, -1)] * len(line))

start = ((0, 0), (0, 1), 0, 0) # coord, dir, current straight length, g_score
end = (len(grid[0]) - 1, len(grid) - 1)

def addMove(a, b):
	return (a[0] + b[0], a[1] + b[1])

def hScore(c):
	global end
	return end[0] - c[0] + end[1] - c[1]

prev = {}

current = [start]
i = 0
while len(current) > 0:
	i += 1
	coord, direction, straight_count, g_score = current.pop(0)

	if coord == end:
		print(i, g_score)
		break

	possible_dirs = [(direction[1], direction[0]), (-direction[1], -direction[0])]
	if straight_count < 3:
		possible_dirs.append(direction)

	for new_dir in possible_dirs:
		new_coord = addMove(coord, new_dir)
		x, y = new_coord

		if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
			continue

		new_g_score = g_score + grid[y][x]
		h_score = hScore(new_coord)

		f_score = new_g_score + h_score

		new_straight_count = (straight_count + 1) if new_dir == direction else 1
		new_c = (new_coord, new_dir, new_straight_count, new_g_score)

		move = (new_coord, new_dir, new_straight_count)

		if move in prev:
			if prev[move] <= new_g_score:
				continue
		prev[move] = new_g_score

		# Binary search to insert sorted
		low = 0
		high = len(current) - 1
		while high - low > 1:
			mid = (high + low) // 2
			c = current[mid]
			cf = c[3] + hScore(c[0])

			if f_score < cf:
				high = mid
			else:
				low = mid

		if high == len(current) - 1:
			current.append(new_c)
		else:
			current.insert(low, new_c)
