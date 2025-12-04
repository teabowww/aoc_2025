class BatteryBank:
	def __init__(self, batteries):
		self.batteries = [int(battery) for battery in batteries]

	def joltage(self, n):
		joltage = 0

		first_digit = max(self.batteries[0:-n])
		index = self.batteries.index(first_digit)
		second_digit = max(self.batteries[index+1:])

		joltage = first_digit * 10 + second_digit
		return joltage

with open("input.txt") as file:
	input_text = file.read()
	banks = input_text.split("\n")

total_joltage = 0

for bank in banks:
	battery_bank = BatteryBank(bank)

	total_joltage += battery_bank.joltage(1)

print(total_joltage)

