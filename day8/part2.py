from math import gcd

input_file = open('input.txt', 'r')

instructions = []

graph = {}

current = []

for line in input_file:
	line = line.rstrip('\n')

	if len(instructions) == 0:
		indexed = 'LR'
		for c in line:
			if c in indexed:
				instructions.append(indexed.index(c))
		continue

	line = line.split()

	if len(line) == 4:
		graph[line[0]] = (line[2][1:-1], line[3][:-1])

		if line[0][-1] == 'A':
			current.append(line[0])

solutions = [-1 for x in current]

steps = 0
while -1 in solutions:
	for i, c in enumerate(current):
		if solutions[i] != -1:
			# Already have a solution for this
			continue


		current[i] = graph[c][instructions[steps % len(instructions)]]
		
		if current[i][-1] == 'Z':
			solutions[i] = steps + 1
	steps += 1

lcm = 1
for s in solutions:
	lcm = lcm * s // gcd(lcm, s)

print(lcm)