def largest_divisor(n):
    d = 1

    for i in range(2, n):
        if n % i == 0:
            d = i
    
    return d

def string_repeats(string, pattern_len):
	str_len = len(string)

	if str_len == 1 or str_len % pattern_len != 0:
		return False

	pattern = string[0:pattern_len]
	
	num_patterns = int(str_len / pattern_len)

	for i in range(1, num_patterns):
		start = i * pattern_len
		end = i * pattern_len + pattern_len

		segment = string[start:end]

		if segment != pattern:
			return False

	return True

def id_valid(id_num):
	id_len = len(id_num)

	max_pattern_len = largest_divisor(id_len)

	for i in range(max_pattern_len, 0, -1):
		if string_repeats(id_num, i):
			print(i)
			return False

	return True

id_sum = 0

with open("input.txt") as file:
	input_text = file.read()
	id_ranges = input_text.split(",")

for id_range in id_ranges:
	range_split = id_range.split("-")
	
	id_min = int(range_split[0])
	id_max = int(range_split[1]) + 1

	for id_num in range(id_min, id_max):
		if not id_valid(str(id_num)):
			id_sum += id_num
			print(id_num)

print(id_sum)
