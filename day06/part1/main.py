import re
import math

input_file = "input.txt"

with open(input_file) as file:
	input_lines = [line.strip() for line in file.readlines()]
	print(input_lines)

nums = [[int(num_string) for num_string in re.split(r'[ ]+', string)] for string in input_lines[0:-1]]
operators = re.split(r'[ ]+', input_lines[-1])

rows = len(input_lines)
cols = len(nums[0])

total = 0

for x in range(cols):
	used_nums = []
	operation = operators[x]

	for y in range(rows - 1):
		used_nums.append(nums[y][x])

	result = 0

	match operation:
		case '+':
			result = sum(used_nums)
		case '*':
			result = math.prod(used_nums)

	print(used_nums, operation, "=", result)

	total += result

print(total)

