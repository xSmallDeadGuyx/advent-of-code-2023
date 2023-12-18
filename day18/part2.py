input_file = open('input.txt', 'r')

dirs = {'2': (-1, 0), '0': (1, 0), '3': (0, -1), '1': (0, 1)}

x = y = 0
area = 0
length = 1
for line in input_file:
	line = line.rstrip('\n').split() 

	# Same as part 1 except the dir is encoded as a num at the end of the hex and the length is the first 5 hex digits
	dx, dy = dirs[line[2][-2]]
	n = int(line[2][2:-2], 16)

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