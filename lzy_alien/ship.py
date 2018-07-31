import pygame

class Ship():
	"""docstring for ClassName"""
	def __init__(self, screen,settings):
		super(Ship, self).__init__()
		self.screen = screen

		self.image = pygame.image.load("images/space_ship.png")

		self.rect = self.image.get_rect()

		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx

		self.rect.bottom = self.screen_rect.bottom

		self.moveright = False

		self.moveleft = False

		self.moveup = False

		self.movedown = False

		self.settings = settings

	def update(self):
		if self.moveright and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.settings.ship_speed

		elif self.moveleft and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= self.settings.ship_speed

		elif self.moveup and self.rect.top > self.screen_rect.top:
			self.rect.centery -= self.settings.ship_speed

		elif self.movedown and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.settings.ship_speed

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		self.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
