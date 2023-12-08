input_file = open('input.txt', 'r')

instructions = []

graph = {}

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

current = 'AAA'

steps = 0
while current != 'ZZZ':
	current = graph[current][instructions[steps % len(instructions)]]
	steps += 1

print(steps)
