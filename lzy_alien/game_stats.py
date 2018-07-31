class GameStats():
	"""docstring for GameStats"""
	def __init__(self, settings):
		super(GameStats, self).__init__()
		self.settings = settings
		self.reset_stats()
		self.game_active = False

	def reset_stats(self):
		self.ships_left = self.settings.ship_limit
		