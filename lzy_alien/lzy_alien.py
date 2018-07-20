import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

	pygame.init()

	settings = Settings()

	screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))

	pygame.display.set_caption("Alien Invasion")

	ship = Ship(screen,settings)

	while True:
		gf.check_events(ship)

		ship.update()

		gf.update_screen(settings,screen,ship)

run_game()