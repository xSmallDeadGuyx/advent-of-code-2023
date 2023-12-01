import re

input_file = open('input.txt', 'r')

total = 0

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def toDigit(word):
	global words

	if word in words:
		return str(words.index(word) + 1)
	else:
		return str(int(word))

for line in input_file:
	line = line.rstrip('\n')

	# Nasty look-ahead regex to handle overlapping matches
	matches = re.findall(r'(?=([0-9]|' + '|'.join(words) + '))', line)
	if len(matches) > 0:
		num = int(toDigit(matches[0]) + toDigit(matches[-1]))
		print(line + ", " + str(num))
		total += num

print(total)
