input_file = open('input.txt', 'r')

wires = {}

for line in input_file:
	line = line.rstrip('\n').split(': ')
	
	fr = line[0]
	to = line[1].split()
	
	if fr in wires:
		wires[fr].extend(to)
	else:
		wires[fr] = to
	
	for t in to:
		if t in wires:
			wires[t].append(fr)
		else:
			wires[t] = [fr]

# Build an initial seed group based on a 3-part flood fill from a node, then expand only with nodes that have >= 2 connections until no more to add
# If the outgoing connections from the group after expanding is 3 then we're done, or very unlucky maybe?
# Works on my input, at least
for seed, seed_to in wires.items():
	group_a = [seed]
	group_a.extend(seed_to)
		
	for node in seed_to:
		for w in wires[node]:
			if w not in group_a:
				group_a.append(w)
				
				for w2 in wires[w]:
					if w2 not in group_a:
						group_a.append(w2)
	
	outgoing = []
	for node in group_a:
		for w in wires[node]:
			if w not in outgoing and w not in group_a:
				outgoing.append(w)
	
	any = True
	while any:
		any = False
		for i, node in enumerate(outgoing):
			c = 0
			new_out = []
			for w in wires[node]:
				if w in group_a:
					c += 1
				else:
					new_out.append(w)
			if c >= 2:
				group_a.append(node)
				del outgoing[i]
				for w in new_out:
					if w not in outgoing:
						outgoing.append(w)
				any = True
				break
	
	if len(outgoing) == 3:
		print(len(group_a))
		print(len(wires) - len(group_a))
		print(len(group_a) * (len(wires) - len(group_a)))
		break
