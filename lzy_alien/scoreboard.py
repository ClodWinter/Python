import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	"""docstring for Scoreboard"""
	def __init__(self, settings,screen,stats):
		super(Scoreboard, self).__init__()

		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = stats

		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)

		self.prep_score()
		self.prep_score_high()
		self.prep_level()
		self.prep_ships()


	def prep_score_high(self):
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
		self.text_color, self.settings.bg_color)
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_score(self):

		rounded = round(self.stats.score,-1)

		score_str = "{:,}".format(rounded)
		self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 10


	def prep_level(self):
		self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.settings.bg_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10


	def prep_ships(self):
		self.ships = Group()
		for number in range(self.stats.ships_left):
			ship = Ship(self.screen,self.settings)
			ship.rect.x = 10 + number * ship.rect.width
			ship.rect.y = 10
			ship.rect.width = 30
			ship.rect.height = 30
			self.ships.add(ship)
		print(1)


	def show_score(self):
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.ships.draw(self.screen)
