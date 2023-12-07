import functools

input_file = open('input.txt', 'r')

buckets = [[], [], [], [], [], [], []]
total_hands = 0

for line in input_file:
	line = line.rstrip('\n').split()

	hand = line[0]
	score = int(line[1])

	cards = {}
	for c in hand:
		cards[c] = cards[c] + 1 if c in cards else 1

	diff_nums = 0
	max_num = 0
	jokers = 0
	for c, n in cards.items():
		if c == 'J':
			jokers = n
		else:
			diff_nums += 1
			max_num = max(max_num, n)

	max_num += jokers

	bucket = 6
	if max_num == 5:
		# 5 of a kind
		bucket = 0
	elif max_num == 4:
		# 4 of a kind
		bucket = 1
	elif diff_nums == 2:
		# Full house
		bucket = 2
	elif max_num == 3:
		# 3 of a kind
		bucket = 3
	elif diff_nums == 3:
		# 2 pairs
		bucket = 4
	elif max_num == 2:
		# 1 pair
		bucket = 5
	else:
		# High card
		bucket = 6

	buckets[bucket].append((hand, score))
	total_hands += 1

card_values = 'AKQT98765432J'

def compare(a, b):
	for i in range(5):
		ac = card_values.index(a[0][i])
		bc = card_values.index(b[0][i])
		if ac < bc:
			return 1
		if ac > bc:
			return -1
	return 0

rank = total_hands
total = 0
for hands in buckets:
	hands.sort(key=functools.cmp_to_key(compare), reverse=True)

	for hand in hands:
		total += rank * hand[1]
		rank -= 1

print(total)
