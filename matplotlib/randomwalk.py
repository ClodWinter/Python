from random import choice

class RandomWalk():
	"""docstring for RandomWalk"""
	def __init__(self, num_points=5000):
		super(RandomWalk, self).__init__()
		self.num_points = num_points

		self.xvalues = [0]
		self.yvalues = [0]


	def fill_walk(self):

		while len(self.xvalues)<self.num_points:
			x_direction = choice([1,-1])
			x_distance = choice([0,1,2,3,4])
			x_step = x_direction*x_distance

			y_direction = choice([1,-1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction*y_distance

			if x_step==0 and y_step==0:
				continue

			next_x = self.xvalues[-1] + x_step
			next_y = self.yvalues[-1] + y_step

			self.xvalues.append(next_x)
			self.yvalues.append(next_y)
