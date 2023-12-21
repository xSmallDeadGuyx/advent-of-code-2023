input_file = open('input.txt', 'r')

grid = []
start = (0, 0)

for line in input_file:
	line = line.rstrip('\n')

	if 'S' in line:
		start = (line.index('S'), len(grid))
	grid.append([1 if c == '#' else 0 for c in line])

count = 0

queue = [(start, 0)]
grid[start[1]][start[0]] = 1

while len(queue) > 0:
	pos, steps = queue.pop(0)

	if steps % 2 == 0:
		count += 1
	if steps == 64:
		continue

	x, y = pos
	for m in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
		mx, my = m

		nx = x + mx
		ny = y + my

		if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
			continue

		if grid[ny][nx] == 1:
			continue

		grid[ny][nx] = 1
		queue.append(((nx, ny), steps + 1))

print(count)
