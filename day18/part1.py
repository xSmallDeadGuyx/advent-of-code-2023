input_file = open('input.txt', 'r')

dirs = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}

x = y = 0
area = 0
length = 1
for line in input_file:
	line = line.rstrip('\n').split() 

	dx, dy = dirs[line[0]]
	n = int(line[1])

	nx = x + dx * n
	ny = y + dy * n

	area += ny * x - nx * y
	length += n

	x = nx
	y = ny

# Shoelace formula for inner area
area = area // 2

# Account for edge of trench
area += length // 2 + 1

print(area)