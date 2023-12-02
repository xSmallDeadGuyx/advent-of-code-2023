import re

input_file = open('input.txt', 'r')

def checkMax(line, colour, value):
	matches = re.findall(r'([0-9]+) ' + colour, line)
	for match in matches:
		if int(match) > value:
			return False
	return True

total = 0
for line in input_file:
	line = line.rstrip('\n')

	if checkMax(line, 'red', 12) and checkMax(line, 'green', 13) and checkMax(line, 'blue', 14):
		total += int(line.split(':')[0][5:])

print(total)
