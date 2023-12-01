import re

input_file = open('input.txt', 'r')

total = 0

for line in input_file:
	line = line.rstrip('\n')

	matches = re.findall(r'[0-9]', line)
	if len(matches) > 0:
		num = int(matches[0] + matches[-1])
		print(line + ", " + str(num))
		total += num

print(total)
