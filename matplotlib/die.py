from random import randint

class Die():
	"""docstring for Die"""
	def __init__(self, num_sides = 6):
		super(Die, self).__init__()
		self.num_sides = num_sides

	def roll(self):
		return randint(1,self.num_sides)
