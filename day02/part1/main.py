def id_valid(id_num):
	id_len = len(id_num)

	if id_len % 2 == 1:
		return True

	id_half_len = int(id_len/2)

	first_half = id_num[0:id_half_len]
	second_half = id_num[id_half_len:]

	return first_half != second_hal

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
