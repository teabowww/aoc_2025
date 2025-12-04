with open("input.txt") as file:
	input_text = file.read()
	banks = input_text.split("\n")

total_joltage = 0

for bank in banks:
	batteries = [int(bank[i:i+1]) for i in range(len(bank))]

	first_digit = max(batteries[0:-1])

	index = batteries.index(first_digit)

	second_digit = max(batteries[index+1:])

	joltage = first_digit * 10 + second_digit

	print(bank, joltage)

	total_joltage += joltage

print(total_joltage)

