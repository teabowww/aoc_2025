def in_ranges(n, ranges):
	for start, end in ranges:
		if start <= n <= end:
			return True

	return False

input_file = "input.txt"

fresh_count = 0

with open(input_file) as file:
	input_string = file.read()
	input_parts = input_string.split("\n\n")

	range_strings = input_parts[0]
	ranges = [tuple(map(int, r.split("-"))) for r in range_strings.split("\n")]

	ids = map(int, input_parts[1].split("\n"))

	for id_num in ids:
		if in_ranges(id_num, ranges):
			fresh_count += 1

print(fresh_count)