# "Fastest" version of part 2 which just uses the quadratic equation
# to find the bound without any iterations, credit to Matt Hill
# (github.com/Lucid-Matt-Hill).

import math

input_file = open('input.txt', 'r')

lines = input_file.readlines()

time = int(''.join(lines[0].split()[1:]))
dist = int(''.join(lines[1].split()[1:]))

# x * (time - x) = distance
# -x^2 + time*x - distance = 0

# Quadratic equation x = (-b +- sqrt(b^2 - 4ac)) / 2a
#   a = -1 so:
# x = (-b +- sqrt(b^2 - 4*-1*c)) / (2 * -1) = (b +- sqrt(b^2 + 4c))/2

b = time
c = -dist

x = (b - math.sqrt(b**2 + 4 * c)) / 2

min_losing_time = math.floor(x)

total_losing_times = min_losing_time * 2 + 1 # Account for time * 0

print(time - total_losing_times)