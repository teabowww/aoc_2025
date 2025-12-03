class DialRotator:
	def __init__(self, rotation, rot_min, rot_max):
		self.rotation = rotation
		self.rot_min = rot_min
		self.rot_max = rot_max
		self.zero_count = 0

	def rotate(self, direction, amount):
		self.rotation += direction * amount

		if self.rotation > self.rot_max:
			self.rotation = self.rotation % (self.rot_max + 1)

		elif self.rotation < self.rot_min:
			self.rotation = (self.rotation + (self.rot_max + 1)) % (self.rot_max + 1)
			
		if self.rotation == 0:
			self.zero_count += 1

rotator = DialRotator(50, 0, 99)

with open("input.txt") as file:
	rotations = file.readlines()

for rot in rotations:
	rot = rot.replace("\n", "")
	
	rot_dir = -1 if rot[0] == "R" else 1
	rot_amount = int(rot[1:])

	rotator.rotate(rot_dir, rot_amount)

print(rotator.zero_count)