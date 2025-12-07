input_file = "input.txt"

with open(input_file) as file:
	input_string = file.read()
	input_parts = input_string.split("\n\n")

range_strings = input_parts[0]
ranges = [tuple(map(int, r.split("-"))) for r in range_strings.split("\n")]

fresh_ids = set()

for start, end in ranges:
	fresh_ids = fresh_ids.union(set(range(start, end+1)))

fresh_id_count = len(fresh_ids)

print(fresh_id_count)