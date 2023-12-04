import re

input_file = open('input.txt', 'r')

def getNums(line):
	return re.split(r'\s+', line.lstrip(' '))

total = 0
for line in input_file:
	line = line.rstrip('\n')

	split_line = line.split(': ')[1].split(' | ')

	to_find = getNums(split_line[0])
	to_search = getNums(split_line[1])
	
	num_winning = len(list(filter(lambda x: x in to_find, to_search)))

	if num_winning > 0:
		total += pow(2, num_winning - 1)

print(total)
