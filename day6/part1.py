input_file = open('input.txt', 'r')

lines = input_file.readlines()

times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))

multi = 1
for i, time in enumerate(times):
	total = 0
	for t in range(1, time + 1):
		if t * (time - t) > distances[i]:
			total += 1
	multi *= total

print(multi)