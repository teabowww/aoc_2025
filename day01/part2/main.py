class DialRotator:
	def __init__(self, rotation, rot_min, rot_max):
		self.rotation = rotation
		self.rot_min = rot_min
		self.rot_max = rot_max
		self.zero_count = 0

	def rotate(self, direction, amount):
		rotation = self.rotation + direction * amount

		self.rotation = rotation % (self.rot_max + 1)

		zero_crosses = abs(int(rotation / (self.rot_max + 1)))
		print("rotation:", rotation)
		print("crosses:", zero_crosses)

		if rotation <= 0:
			zero_crosses += 1
			
		self.zero_count += zero_crosses

		

rotator = DialRotator(50, 0, 99)

rotator.rotate(-1, 50)
rotator.rotate(-1, 50)
#print(rotator.rotation)

"""
with open("input.txt") as file:
	rotations = file.readlines()

for rot in rotations:
	rot = rot.replace("\n", "")
	
	rot_dir = -1 if rot[0] == "L" else 1
	rot_amount = int(rot[1:])

	rotator.rotate(rot_dir, rot_amount)
"""

print("zero crosses:", rotator.zero_count)