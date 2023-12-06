input_file = open('input.txt', 'r')

lines = input_file.readlines()

time = int(''.join(lines[0].split()[1:]))
dist = int(''.join(lines[1].split()[1:]))

total = 0
for t in range(1, time + 1):
	if t * (time - t) > dist:
		total += 1

print(total)