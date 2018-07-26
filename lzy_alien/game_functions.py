import sys
import pygame
from bullet import Bullet
from alien_enemy import Alien

def check_keydown_events(event,settings,screen,ship,bullets):

	if event.key == pygame.K_RIGHT:
		ship.moveright = True
	elif event.key == pygame.K_LEFT:
		ship.moveleft = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		

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
				

def update_screen(settings,screen,ship,bullets,aliens):

	screen.fill(settings.bg_color)

	for bullet in bullets.sprites():
		bullet.drawbullet()

	ship.blitme()

	aliens.draw(screen)

	pygame.display.flip()#刷新屏幕

def update_bullets(bullets):
	bullets.update()

	for bullet in bullets.copy():
			if bullet.rect.bottom<=0:
				bullets.remove(bullet)


def update_aliens(settings,aliens):
	checkAliensEdges(settings,aliens)
	aliens.update()

def fire_bullet(settings,screen,ship,bullets):
	if len(bullets) < settings.bulletcount:
			bullet = Bullet(settings,screen,ship)
			bullets.add(bullet)

def createAliens(settings,screen,ship,aliens):
	alien = Alien(settings,screen)
	alien_width = alien.rect.width
	number_column = getAlienColumnWithWidth(settings,alien_width)
	number_row = getAlienRowsWithHeight(settings,ship.rect.height,alien.rect.height)

	for row in range(0,number_row):
		for number in range(0,number_column):
			createAlien(settings,screen,aliens,number,row)

	

def getAlienColumnWithWidth(settings,alien_width):
	space_x = settings.screen_width - 2*alien_width
	number_alien = int(space_x / (2*alien_width))
	return number_alien

def getAlienRowsWithHeight(settings,ship_height,alien_height):
	space_y = settings.screen_height - 3*alien_height - ship_height
	return int(space_y/(2*alien_height))

def createAlien(settings,screen,aliens,column,row):
	alien = Alien(settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width*column
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row
	aliens.add(alien)

def checkAliensEdges(settings,aliens):
	for alien in aliens.sprites():
		if alien.checkEdges():
			changeAliensDirection(settings,aliens)
			break

def changeAliensDirection(settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y += settings.alien_down_speed
	settings.alien_direction *= -1
				
