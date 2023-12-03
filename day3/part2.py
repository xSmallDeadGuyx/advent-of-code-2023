input_file = open('input.txt', 'r')

nums = []
gears = []

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

			if c == '*':
				gears.append((x, y))
		x += 1
		
	if building_num[0] != 0:
		nums.append(building_num)

	y += 1

total = 0
for gear in gears:
	adj_nums = []
	for num in nums:
		for num_coord in num[1]:
			if abs(num_coord[0] - gear[0]) <= 1 and abs(num_coord[1] - gear[1]) <= 1:
				adj_nums.append(num[0])
				break

	if len(adj_nums) == 2:
		total += adj_nums[0] * adj_nums[1]

print(total)
