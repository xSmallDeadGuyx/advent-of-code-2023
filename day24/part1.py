input_file = open('input.txt', 'r')

min_pos = 200000000000000
max_pos = 400000000000000

hail = []

count = 0
for line in input_file:
	line = line.rstrip('\n').split(' @ ')

	px, py, pz = map(int, line[0].split(', '))
	vx, vy, vz = map(int, line[1].split(', '))

	for op, ov in hail:
		opx, opy, opz = op
		ovx, ovy, ovz = ov

		# px + vx * t1 = opx + ovx * t2
		# py + vy * t1 = opy + ovy * t2

		# t1 = (ovy * t2 + opy - py) / vy

		# px + vx * (ovy * t2 + opy - py) / vy = opx + ovx * t2
		# (vx / vy * ovy - ovx) * t2 = opx - px - (opy - py) * vx / vy

		if vx / vy * ovy == ovx:
			continue

		t2 = (opx - px - (opy - py) * vx / vy) / (vx / vy * ovy - ovx)
		t1 = (opx + ovx * t2 - px) / vx

		if t1 < 0 or t2 < 0:
			continue

		cx = opx + ovx * t2
		cy = opy + ovy * t2

		if cx >= min_pos and cy >= min_pos and cx <= max_pos and cy <= max_pos:
			count += 1

	hail.append(((px, py, pz), (vx, vy, vz)))

print(count)