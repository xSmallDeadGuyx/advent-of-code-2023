input_file = open('input.txt', 'r')

total = 0
for line in input_file:
	line = line.rstrip('\n')

	nums = list(map(int, line.split()))
	
	while nums.count(0) < len(nums):
		total += nums[-1]
		nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

print(total)