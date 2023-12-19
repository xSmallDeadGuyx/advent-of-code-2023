input_file = open('input.txt', 'r')

ops = {'<': lambda a, b: a < b, '>': lambda a, b: a > b}

wfs = {}

total = 0
parsing_wfs = True
for line in input_file:
	line = line.rstrip('\n')

	if len(line) == 0:
		parsing_wfs = False
		continue

	if parsing_wfs:
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
		obj = {}
		for part in line[1:-1].split(','):
			obj[part[0]] = int(part[2:])

		cur = 'in'
		while cur not in 'AR':
			wf = wfs[cur]

			for rule in wf:
				if len(rule) == 1:
					cur = rule[0]
					break
				elif ops[rule[1]](obj[rule[0]], rule[2]):
					cur = rule[3]
					break

		if cur == 'A':
			total += sum(v for s, v in obj.items())

print(total)