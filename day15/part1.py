input_file = open('input.txt', 'r')

total = 0
for line in input_file:
	line = line.rstrip('\n')
	
	for s in line.split(','):
		hash = 0
		for c in s:
			hash = ((hash + ord(c)) * 17) % 256
		
		total += hash
		
print(total)
