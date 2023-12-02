import re

input_file = open('input.txt', 'r')

def getMax(line, colour):
	matches = re.findall(r'([0-9]+) ' + colour, line)
	return max(map(int, matches))

total = 0
for line in input_file:
	line = line.rstrip('\n')

	total += getMax(line, 'red') * getMax(line, 'green') * getMax(line, 'blue')

print(total)
