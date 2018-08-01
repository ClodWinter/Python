class Settings():
	"""docstring for ClassName"""
	def __init__(self):
		super(Settings, self).__init__()
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230,230,230)
		self.ship_speed = 5

		self.bulletspeed = 5
		self.bulletwidth = 300
		self.bulletheight = 15
		self.bulletcolor = 3,60,60
		self.bulletcount = 3
		self.alien_down_speed = 10
		self.alien_direction = 1
		self.alien_speed = 1

		self.ship_limit = 3

		self.speedup_scale = 1.1

		self.score_scale = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		self.ship_speed = 5
		self.bulletspeed = 5
		self.alien_speed = 1
		self.alien_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bulletspeed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points*self.score_scale)