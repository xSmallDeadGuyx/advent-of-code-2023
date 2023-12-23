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

disintegratable = [True] * len(bricks)
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

	if len(at_max_z) == 1:
		disintegratable[at_max_z[0]] = False

	new_lz = max_z + 1
	new_hz = hz - (lz - new_lz)
	settled.append(((lx, ly, new_lz), (hx, hy, new_hz)))

print(disintegratable.count(True))
