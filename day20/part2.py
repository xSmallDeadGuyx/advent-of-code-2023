from math import gcd

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

# From visualizing input, there are 4 cycles which are long chains of 12 nodes in a row with some of these nodes in the chain connecting to a single convolution.
# These 4 convolutions effectively then "cycle" on a single state of these 12 nodes, or a 12-bit number if we treat each node as a bit.
# If we simply iterate up to the first time the 12th bit flips, at 2048, we can figure out the cycles of each input into the convolution to get which bits are required.
# Adding all these bits gives us the 12-bit cycle number.
# LCM of all 4 cycle numbers is our answer.

cycles = {}
cycles['qx'] = memories['qx'].copy()
cycles['db'] = memories['db'].copy()
cycles['vc'] = memories['vc'].copy()
cycles['gf'] = memories['gf'].copy()

i = 0
while i < 2048:
	i += 1

	queue = []
	for to in broadcast:
		queue.append(('broadcaster', to, 0))

	while len(queue) > 0:
		f, t, p = queue.pop(0)

		if t == 'zl' and p == 0:
			print('zl', i)

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

	for n, c in cycles.items():
		for m, v in c.items():
			if v > 0:
				continue
			if memories[n][m] == 1:
				cycles[n][m] = i

	if all(list(c.values()).count(0) == 0 for c in cycles.values()):
		break

l = 1
for conv, c in cycles.items():
	s = sum(c.values())
	print(conv, s)
	
	l = l * s // gcd(l, s)

print(l)