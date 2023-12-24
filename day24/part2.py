from z3 import *

input_file = open('input.txt', 'r')

hail = []

i = 0
for line in input_file:
	i += 1
	if i > 3:
		break

	line = line.rstrip('\n').split(' @ ')

	px, py, pz = map(int, line[0].split(', '))
	vx, vy, vz = map(int, line[1].split(', '))

	hail.append(((px, py, pz), (vx, vy, vz)))

# I did the linear equations manually for part 1, but 6 unknown variables is too many to bother.
# Let's use a solver.

x = Int('x')
y = Int('y')
z = Int('z')
vx = Int('vx')
vy = Int('vy')
vz = Int('vz')

s = Solver()

i = 0
for hp, hv in hail:
	i += 1
	t = Int('t' + str(i))

	hx, hy, hz = hp
	hvx, hvy, hvz = hv
	s.add(x + vx * t == hx + hvx * t)
	s.add(y + vy * t == hy + hvy * t)
	s.add(z + vz * t == hz + hvz * t)

print(s.check())
m = s.model()
print(m)

print(m[x].as_long() + m[y].as_long() + m[z].as_long())
