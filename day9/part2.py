input_file = open('input.txt', 'r')

total = 0
for line in input_file:
	line = line.rstrip('\n')

	nums = list(map(int, line.split()))

	prev_nums = []
	
	while nums.count(0) < len(nums):
		prev_nums.insert(0, nums)
		nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

	new = 0
	for nums in prev_nums:
		new = nums[0] - new
	total += new

print(total)