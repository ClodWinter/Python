import sys
import pygame
from bullet import Bullet
from alien_enemy import Alien
from time import sleep

def check_keydown_events(event,settings,screen,ship,bullets):

	if event.key == pygame.K_RIGHT:
		ship.moveright = True
	elif event.key == pygame.K_LEFT:
		ship.moveleft = True
	elif event.key == pygame.K_UP:
		ship.moveup = True
	elif event.key == pygame.K_DOWN:
		ship.movedown = True

	elif event.key == pygame.K_SPACE:
		fire_bullet(settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_play_button(settings,screen,stats,playbutton,ship,aliens,bullets,x,y):
	
	if playbutton.rect.collidepoint(x,y):
		stats.reset_stats()
		stats.game_active = True
		aliens.empty()
		bullets.empty()
		createAliens(settings,screen,ship,aliens)
		ship.center_ship()

def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moveright = False
	elif event.key == pygame.K_LEFT:
		ship.moveleft = False
	elif event.key == pygame.K_UP:
		ship.moveup = False
	elif event.key == pygame.K_DOWN:
		ship.movedown = False

def check_events(settings,screen,ship,aliens,bullets,playbutton,stats):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,settings,screen,ship,bullets)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				x,y = pygame.mouse.get_pos()
				check_play_button(settings,screen,stats,playbutton,ship,aliens,bullets,x,y)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)
				

def update_screen(settings,stats,screen,ship,bullets,aliens,playbutton):

	screen.fill(settings.bg_color)

	for bullet in bullets.sprites():
		bullet.drawbullet()

	ship.blitme()

	aliens.draw(screen)

	if not stats.game_active:
		playbutton.draw_button()

	pygame.display.flip()#刷新屏幕

def update_bullets(settings,screen,ship,aliens,bullets):
	bullets.update()
	for bullet in bullets.copy():
			if bullet.rect.bottom<=0:
				bullets.remove(bullet)

	check_bullets_alien_collisions(settings,screen,ship,aliens,bullets)


def check_bullets_alien_collisions(settings,screen,ship,aliens,bullets):
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

	if len(aliens) == 0:
		bullets.empty()
		createAliens(settings,screen,ship,aliens)


def update_aliens(settings,stats,screen,ship,aliens,bullets):
	checkAliensEdges(settings,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(settings,stats,screen,ship,aliens,bullets)
	check_aliens_bottom(settings,stats,screen,ship,aliens,bullets)

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

def ship_hit(settings,stats,screen,ship,aliens,bullets):

	if stats.ships_left > 0:
		stats.ships_left -= 1
		aliens.empty()
		bullets.empty()
		createAliens(settings,screen,ship,aliens)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active = False

	

def check_aliens_bottom(settings,stats,screen,ship,aliens,bullets):
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen.get_rect().bottom:
			ship_hit(settings,stats,screen,ship,aliens,bullets)
			break
				
