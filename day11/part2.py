input_file = open('input.txt', 'r')

galaxies = []

empty_rows = []
empty_cols = []

y = 0
for line in input_file:
	line = line.rstrip('\n')

	x = 0
	is_empty = True
	for c in line:
		if c == '#':
			is_empty = False
			galaxies.append((x, y))
			if y != 0 and x in empty_cols:
				empty_cols.remove(x)
		elif y == 0:
			empty_cols.append(x)
		x += 1

	if is_empty:
		empty_rows.append(y)

	y += 1

def diffAxis(a, b, empty):
	min_axis = min(a, b)
	max_axis = max(a, b)
	diff = max_axis - min_axis
	for e in empty:
		if min_axis < e and e < max_axis:
			diff += 999999

	return diff

total = 0
for i in range(len(galaxies) - 1):
	a = galaxies[i]
	for j in range(i + 1, len(galaxies)):
		if i == j:
			continue

		b = galaxies[j]

		total += diffAxis(a[0], b[0], empty_cols)
		total += diffAxis(a[1], b[1], empty_rows)

print(total)