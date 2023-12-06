# "Fast" version of part 2 which drops from 54 million iterations to
# "only" 400k by searching from a more sensible start value and
# calculating the rest from a single bound.

input_file = open('input.txt', 'r')

lines = input_file.readlines()

time = int(''.join(lines[0].split()[1:]))
dist = int(''.join(lines[1].split()[1:]))

min_winning_time = int(dist / time) + 1
for t in range(min_winning_time, int(time / 2)):
	if t * (time - t) > dist:
		min_winning_time = t
		break

min_losing_time = min_winning_time - 1
total_losing_times = min_losing_time * 2 + 1 # Account for time * 0

print(time - total_losing_times)