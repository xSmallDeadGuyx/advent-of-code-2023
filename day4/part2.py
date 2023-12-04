import re

input_file = open('input.txt', 'r')

def getNums(line):
	return re.split(r'\s+', line.lstrip(' '))

winnings = []

for line in input_file:
	line = line.rstrip('\n')

	split_line = line.split(': ')[1].split(' | ')

	to_find = getNums(split_line[0])
	to_search = getNums(split_line[1])
	
	num_winning = len(list(filter(lambda x: x in to_find, to_search)))

	winnings.append(num_winning)

copies = [1 for x in winnings]

for i in range(len(winnings)):
	if winnings[i] > 0:
		for j in range(winnings[i]):
			copies[i + j + 1] += copies[i]

print(sum(copies))
