# "Faster" version of part 2 which drops from 400k iterations to 25
# by doing a binary search for the lower bound.

input_file = open('input.txt', 'r')

lines = input_file.readlines()

time = int(''.join(lines[0].split()[1:]))
dist = int(''.join(lines[1].split()[1:]))

lower_bound = int(dist / time)
upper_bound = int(time / 2)

iters = 0
while upper_bound - lower_bound > 1:
	iters += 1
	x = int((upper_bound + lower_bound) / 2)
	if x * (time - x) > dist:
		upper_bound = x
	else:
		lower_bound = x

total_losing_times = lower_bound * 2 + 1 # Account for time * 0

print(time - total_losing_times)