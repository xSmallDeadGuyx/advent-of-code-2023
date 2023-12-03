input_file = open('input.txt', 'r')

nums = []
symbols = []

y = 0
for line in input_file:
	line = line.rstrip('\n')

	building_num = [0, []] # value, coords
	x = 0
	for c in line:
		if c.isnumeric():
			building_num[0] = building_num[0] * 10 + int(c)
			building_num[1].append((x, y))
		else:
			if building_num[0] != 0:
				nums.append(building_num)
				building_num = [0, []]

			if c != '.':
				symbols.append((x, y))
		x += 1

	if building_num[0] != 0:
		nums.append(building_num)


	y += 1

def nextToSymbol(num):
	for num_coord in num[1]:
		for symbol_coord in symbols:
			if abs(num_coord[0] - symbol_coord[0]) <= 1 and abs(num_coord[1] - symbol_coord[1]) <= 1:
				return True
	return False

nums = filter(nextToSymbol, nums)

total = 0
for num in nums:
	total += num[0]

print(total)
