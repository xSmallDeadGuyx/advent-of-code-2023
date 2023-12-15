input_file = open('input.txt', 'r')

boxes = [[] for i in range(256)]

for line in input_file:
	line = line.rstrip('\n')
	
	for s in line.split(','):
		label = ''
		hash = 0
		for c in s:
			if c in '-=':
				break
			label += c
			hash = ((hash + ord(c)) * 17) % 256
		
		if s[-1] in '123456789':
			lens = int(s[-1])
			
			found = False
			for i, l in enumerate(boxes[hash]):
				if l[0] == label:
					boxes[hash][i] = (label, lens)
					found = True
					break
			if not found:
				boxes[hash].append((label, lens))
			
		else:
			for i, l in enumerate(boxes[hash]):
				if l[0] == label:
					del boxes[hash][i]
					break

total = 0
for i, box in enumerate(boxes):
	for j, lens in enumerate(box):
		total += (i + 1) * (j + 1) * lens[1]
print(total)
