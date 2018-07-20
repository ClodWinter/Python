import sys
import pygame

def check_keydown_events(event,ship):

	if event.key == pygame.K_RIGHT:
		ship.moveright = True
	elif event.key == pygame.K_LEFT:
		ship.moveleft = True

def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moveright = False
	elif event.key == pygame.K_LEFT:
		ship.moveleft = False

def check_events(ship):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,ship)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)
				

def update_screen(settings,screen,ship):

	screen.fill(settings.bg_color)

	ship.blitme()

	pygame.display.flip()#刷新屏幕