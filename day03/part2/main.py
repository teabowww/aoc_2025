class BatteryBank:
	def __init__(self, batteries):
		self.batteries = [int(battery) for battery in batteries]

	def joltage(self, n):
		joltage = 0
		start_index = 0
		end_index = -n

		for i in range(n+1):
			if end_index == 0:
				end_index = None

			digit = max(self.batteries[start_index:end_index])
			joltage += digit * pow(10, n - i)

			start_index = self.batteries.index(digit) + 1
			if end_index: end_index += 1

			print(start_index, end_index)

		return joltage

input_file = "sample.txt"

with open(input_file) as file:
	input_text = file.read()
	banks = input_text.split("\n")

total_joltage = 0

for bank in banks:
	battery_bank = BatteryBank(bank)

	joltage = battery_bank.joltage(11)

	total_joltage += joltage

	print(bank, joltage)

print(total_joltage)

