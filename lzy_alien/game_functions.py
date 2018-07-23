import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,settings,screen,ship,bullets):

	if event.key == pygame.K_RIGHT:
		ship.moveright = True
	elif event.key == pygame.K_LEFT:
		ship.moveleft = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings,screen,ship,bullets)
		

def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moveright = False
	elif event.key == pygame.K_LEFT:
		ship.moveleft = False

def check_events(settings,screen,ship,bullets):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,settings,screen,ship,bullets)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)
				

def update_screen(settings,screen,ship,bullets):

	screen.fill(settings.bg_color)

	for bullet in bullets.sprites():
		bullet.drawbullet()

	ship.blitme()

	pygame.display.flip()#刷新屏幕

def update_bullets(bullets):
	bullets.update()

	for bullet in bullets.copy():
			if bullet.rect.bottom<=0:
				bullets.remove(bullet)

def fire_bullet(settings,screen,ship,bullets):
	if len(bullets) < settings.bulletcount:
			bullet = Bullet(settings,screen,ship)
			bullets.add(bullet)
