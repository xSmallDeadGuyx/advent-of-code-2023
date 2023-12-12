import functools
import re

input_file = open('input.txt', 'r')

@functools.cache
def countValid(line, nums, current_count=0):
	if len(line) == 0:
		if len(nums) == 1 and nums[0] == current_count:
			# Last number satisfied
			return 1
		if len(nums) == 0 and current_count == 0:
			# No number left to find
			return 1

		# Either we have broken springs and no count for them or a count with no broken springs left
		return 0

	if len(nums) == 0:
		return '#' not in line

	spring = line[0]
	line = line[1:]

	current_num = nums[0]

	if spring == '.':
		if current_count == 0:
			# Not counting any number, skip over unbroken spring
			return countValid(line, nums, 0)
		elif current_count == current_num:
			# Current counting number satisfied, start next
			return countValid(line, nums[1:], 0)

		# Current count is unsatisfied and hit an unbroken spring
		return 0
	elif spring == '#':
		if current_count >= current_num:
			# Found another broken spring longer than the current count
			return 0
		# Start/continue current count
		return countValid(line, nums, current_count + 1)
	elif spring == '?':
		# Try both broken and unbroken spring
		return countValid('#' + line, nums, current_count) + countValid('.' + line, nums, current_count)

total = 0
for line in input_file:
	line = line.rstrip('\n').split()

	nums = tuple(map(int, line[1].split(',')))

	total += countValid('?'.join([line[0]] * 5), nums * 5)

print(total)
