input_file = open('input.txt', 'r')

grid = []
start = (0, 0)

for line in input_file:
	line = line.rstrip('\n')

	if 'S' in line:
		start = (line.index('S'), len(grid))
	grid.append([1 if c == '#' else 0 for c in line])

even_count = 0
even_corners = 0
odd_count = 0
odd_corners = 0

queue = [(start, 0)]
grid[start[1]][start[0]] = 1

while len(queue) > 0:
	pos, steps = queue.pop(0)

	if steps % 2 == 0:
		even_count += 1
		if steps > start[0]:
			even_corners += 1
	else:
		odd_count += 1
		if steps > start[0]:
			odd_corners += 1

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


# Since len(grid) is odd, there is a repeating pattern of squares which effectively track odd step count and even step count separately and grids with corners removed (or just individual corners) at the edges.
# 
# Visualisation of grid with corners added/removed if n = 2:
#
# ... ... .O. ... ...
# ... ... OOO ... ...
# ... ..E OOO E.. ...
#
# ... .OO EEE OO. ...
# ... OOO EEE OOO ...
# ..E OOO EEE OOO E..
#
# .OO EEE OOO EEE OO.
# OOO EEE OSO EEE OOO
# .OO EEE OOO EEE OO.
#
# ..E OOO EEE OOO E..
# ... OOO EEE OOO ...
# ... .OO EEE OO. ...
#
# ... ..E OOO E.. ...
# ... ... OOO ... ...
# ... ... .O. ... ...
#
# Instead of counting each individual corner, we can count all 4 corners in 1 go and just reduce the math. So the count of full grids is n*n even step grids and (n-1)*(n-1) odd step grids.
# Then there are 4 * n of each even step grid corner, or just n copies of all 4 corners.
# Then there are (n-1) * 4 odd grids with a single odd corner taken out, which we can calculate as (n-1) * 4 full odd grids - (n-1) * odd_corners.
# Finally the 4 individual edge grids are odd steps with 2 corners missing each, totalling 2 * each corner.
# So in total we have n^2 full even grids + n even corners. Then (n - 1)^2 + 4 * n = n^2 + 2n - 1 full odd grids, minus (n + 1) odd corners.

n = (26501365 - start[0]) // len(grid)
n_sqr = n * n
total = n_sqr * even_count + n * even_corners + (n_sqr + 2 * n + 1) * odd_count - (n + 1) * odd_corners

print(total)
