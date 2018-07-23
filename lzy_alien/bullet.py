import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""docstring for Bullet"""
	def __init__(self, settings,screen,ship):
		super(Bullet, self).__init__()
		self.screen = screen
		self.rect = pygame.Rect(0,0,settings.bulletwidth,settings.bulletheight)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)
		self.color = settings.bulletcolor
		self.bulletspeed = settings.bulletspeed;
	
	def update(self):
		self.y -= self.bulletspeed
		self.rect.y = self.y

	def drawbullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)