input_file = open('input.txt', 'r')

grid = []
energies = []

for line in input_file:
	line = line.rstrip('\n')

	grid.append([c for c in line])
	energies.append([[] for x in line])

def doMove(a, b):
	return (a[0] + b[0], a[1] + b[1])

def addBeam(beam):
	global energies, moving_beams
	x, y = beam[0]
	
	# Ignore beam if we have already simulated this direction in this position
	if beam[1] in energies[y][x]:
		return

	energies[y][x].append(beam[1])
	moving_beams.append(beam)

edges = []
for x in range(len(grid[0])):
	edges.append(((x, -1), (0, 1)))
	edges.append(((x, len(grid)), (0, -1)))
for y in range(len(grid)):
	edges.append(((-1, y), (1, 0)))
	edges.append(((len(grid[0]), y), (-1, 0)))

best = 0
for edge in edges:
	moving_beams = [edge]
	while len(moving_beams) > 0:
		beam = moving_beams.pop()

		new_pos = doMove(beam[0], beam[1])
		x, y = new_pos

		if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
			continue

		c = grid[y][x]

		dx, dy = beam[1]
		new_straight = (new_pos, beam[1])

		if c == '.':
			addBeam(new_straight)
		elif c == '|':
			if dx != 0:
				addBeam((new_pos, (0, -1)))
				addBeam((new_pos, (0, 1)))
			else:
				addBeam(new_straight)
		elif c == '-':
			if dy != 0:
				addBeam((new_pos, (-1, 0)))
				addBeam((new_pos, (1, 0)))
			else:
				addBeam(new_straight)
		elif c == '/':
			addBeam((new_pos, (-dy, -dx)))
		elif c == '\\':
			addBeam((new_pos, (dy, dx)))

	total = 0
	for y, row in enumerate(energies):
		for x, e in enumerate(row):
			if len(e) > 0:
				total += 1
				energies[y][x] = []

	best = max(best, total)
	
print(best)
