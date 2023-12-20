input_file = open('input.txt', 'r')

broadcast = []
ffs = {}
convs = {}
			
for line in input_file:
	line = line.rstrip('\n').split()

	targets = [x.rstrip(',') for x in line[2:]]

	if line[0] == 'broadcaster':
		broadcast = targets
	elif line[0][0] == '%':
		ffs[line[0][1:]] = (0, targets)
	elif line[0][0] == '&':
		convs[line[0][1:]] = targets

memories = {}
for conv in convs.keys():
	memory = {}
	for ff, data in ffs.items():
		if conv in data[1]:
			memory[ff] = 0
	for oc, targets in convs.items():
		if conv in targets:
			memory[oc] = 0
	memories[conv] = memory

total_low = 0
total_high = 0

for i in range(1000):
	total_low += 1 # Initial broadcast

	queue = []
	for to in broadcast:
		queue.append(('broadcaster', to, 0))

	while len(queue) > 0:
		f, t, p = queue.pop(0)

		total_low += 1 - p
		total_high += p

		if t in ffs:
			if p == 0:
				ffs[t] = (1 - ffs[t][0], ffs[t][1])
				for nt in ffs[t][1]:
					queue.append((t, nt, ffs[t][0]))
		else:
			if t in convs:
				memories[t][f] = p

				send_low = sum(memories[t].values()) == len(memories[t].values())
				for nt in convs[t]:
					queue.append((t, nt, 0 if send_low else 1))

print(total_low * total_high)
