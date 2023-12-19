input_file = open('input.txt', 'r')

wfs = {}

def countValid(obj, start):
	global wfs

	count = 0
	cur = start
	while cur not in 'AR':
		wf = wfs[cur]

		for rule in wf:
			if len(rule) == 1:
				cur = rule[0]
				break
			else:
				vals = obj[rule[0]]
				if rule[1] == '<':
					if rule[2] > vals[1]:
						# Entire range contained
						cur = rule[3]
						break
					elif rule[2] <= vals[0]:
						# None of range contained
						continue
					else:
						# Make new ranges and branch to new workflow
						new_obj = obj.copy()
						new_obj[rule[0]] = (vals[0], rule[2] - 1)
						count += countValid(new_obj, rule[3])

						# Leftovers keep simulating in this workflow
						obj[rule[0]] = (rule[2], vals[1])
				else:
					if rule[2] < vals[0]:
						# Entire range contained
						cur = rule[3]
						break
					elif rule[2] >= vals[1]:
						# None of range contained
						continue
					else:
						# Make new ranges and branch to new workflow
						new_obj = obj.copy()
						new_obj[rule[0]] = (rule[2] + 1, vals[1])
						count += countValid(new_obj, rule[3])

						# Leftovers keep simulating in this workflow
						obj[rule[0]] = (vals[0], rule[2])

	if cur == 'A':
		total = 1
		for s, v in obj.items():
			total *= v[1] - v[0] + 1
		count += total
	return count


for line in input_file:
	line = line.rstrip('\n')

	if len(line) > 0:
		line = line.split('{')

		rules = line[1][:-1].split(',')

		parsed = []
		for rule in rules:
			rule = rule.split(':')

			if len(rule) == 1:
				parsed.append((rule[0],))
			else:
				to = rule[1]
				part = rule[0][0]
				op = rule[0][1]
				val = int(rule[0][2:])
				parsed.append((part, op, val, to))

		wfs[line[0]] = parsed
	else:
		start_obj = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
		print(countValid(start_obj, 'in'))
		break