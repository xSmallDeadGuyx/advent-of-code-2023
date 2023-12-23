from heapq import *

input_file = open('input.txt', 'r')

bricks = []

for line in input_file:
	line = line.rstrip('\n').split('~')

	l = tuple(map(int, line[0].split(',')))
	h = tuple(map(int, line[1].split(',')))

	# Put min z first for heappush to sort by min z
	brick = (l[2], l, h)

	heappush(bricks, brick)

supporting = [[] for b in bricks]
supported_by = [[] for b in bricks]
settled = []
while len(bricks) > 0:
	_, l, h = heappop(bricks)

	lx, ly, lz = l
	hx, hy, hz = h

	if lz == 1:
		settled.append((l, h))
		continue

	max_z = 0
	at_max_z = []
	for i, s in enumerate(settled):
		sl, sh = s

		slx, sly, slz = sl
		shx, shy, shz = sh

		if lx <= shx and hx >= slx and ly <= shy and hy >= sly:
			if shz > max_z:
				max_z = shz
				at_max_z = [i]
			elif shz == max_z:
				at_max_z.append(i)

	for i in at_max_z:
		supporting[i].append(len(settled))
		supported_by[len(settled)].append(i)

	new_lz = max_z + 1
	new_hz = hz - (lz - new_lz)
	settled.append(((lx, ly, new_lz), (hx, hy, new_hz)))

total = 0
for i in range(len(supporting)):
	gone = [i]

	sup_by_copy = [s[:] for s in supported_by]

	while len(gone) > 0:
		cur = gone.pop(0)
		for b in supporting[cur]:
			sup_by_copy[b].remove(cur)
			if len(sup_by_copy[b]) == 0:
				gone.append(b)
				total += 1

print(total)