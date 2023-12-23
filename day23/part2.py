import sys
sys.setrecursionlimit(1000000)

input_file = open('input.txt', 'r')

grid = []

for line in input_file:
	line = line.rstrip('\n')

	grid.append([c for c in line])

start = (1, 0)
end = (len(grid[0]) - 2, len(grid) - 1)

visited = [[False] * len(row) for row in grid]

nodes = {}
nodes[start] = []
nodes[end] = []

branches = []

def buildBranch(branch):
	global grid, visited, branches

	x, y = branch[-1]

	visited[y][x] = True

	exits = []

	for mx, my in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
		nx = x + mx
		ny = y + my

		if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
			continue

		if grid[ny][nx] == '#':
			continue

		if (nx, ny) in branch:
			continue

		if (nx, ny) in nodes:
			# Connecting to another branch, save the connection
			connecting = branch[:]
			connecting.append((nx, ny))
			branches.append(connecting)
			return

		if visited[ny][nx]:
			continue

		n = (nx, ny)

		# Exit branch
		if n == end:
			branch.append(n)
			branches.append(branch)
			return

		exits.append(n)

	if len(exits) == 0:
		# Dead end, discard branch
		return
	elif len(exits) == 1:
		# Middle of branch, continue
		ex, ey = exits[0]
		visited[ey][ex] = True
		branch.append(exits[0])
		buildBranch(branch)
	else:
		# End of branch, store and start new branches for each exit
		branches.append(branch)
		nodes[(x, y)] = []
		for exit in exits:
			buildBranch([(x, y), exit])

buildBranch([start])

for i, b in enumerate(branches):
	s = b[0]
	e = b[-1]

	nodes[s].append((e, len(b) - 1))
	nodes[e].append((s, len(b) - 1))

def takeBranch(branch_end, path, steps):
	global nodes

	if branch_end == end:
		return steps

	highest = -1
	for n, l in nodes[branch_end]:
		if n in path:
			continue

		new_steps = steps + l
		new_path = path[:]
		new_path.append(n)
		highest = max(highest, takeBranch(n, new_path, new_steps))

	return highest


print(takeBranch(start, [], 0))
