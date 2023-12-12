import re

input_file = open('input.txt', 'r')

def getPerms(line, nums, needed):
	have = line.count('#')

	if have == needed:
		# Check for correctness
		if re.search('[^#]+'.join('#{' + str(num) + '}' for num in nums), line):
			return 1
		else:
			return 0
	elif line.count('?') >= needed - have:
		# There are enough unknowns to continue
		if re.search('[^#]+'.join('[#?]{' + str(num) + '}' for num in nums), line):
			# The unknowns are in the right places, recursively test them
			return getPerms(line.replace('?', '#', 1), nums, needed) + getPerms(line.replace('?', '.', 1), nums, needed)

	# No correct possibilities from here
	return 0

total = 0
for line in input_file:
	line = line.rstrip('\n').split()

	nums = list(map(int, line[1].split(',')))

	needed = sum(nums)

	total += getPerms(line[0], nums, needed)

print(total)
