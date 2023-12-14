input_file = open('input.txt', 'r')

grid = []
counts = []

for line in input_file:
	line = line.rstrip('\n')

	grid.append([2 if c == '#' else 0 for c in line])
	counts.append(0)

	for x, c in enumerate(line):
		if c == 'O':
			test_y = len(grid) - 2
			while test_y > -1 and grid[test_y][x] == 0:
				test_y -= 1

			grid[test_y + 1][x] = 1
			counts[test_y + 1] += 1

total = 0
for i, c in enumerate(counts):
	total += (len(counts) - i) * c

print(total)
