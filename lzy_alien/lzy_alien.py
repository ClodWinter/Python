import pygame
import sys
import importlib
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien_enemy import Alien
import io
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():  

	pygame.init()

	settings = Settings()

	screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))

	pygame.display.set_caption("lzy-alien")

	ship = Ship(screen,settings)

	bullets = Group()

	aliens = Group()

	stats = GameStats(settings)

	sb = Scoreboard(settings,screen,stats)

	gf.createAliens(settings,screen,ship,aliens)

	play_button = Button(settings,screen,"Play")
        
	while True:
		gf.check_events(settings,screen,ship,aliens,bullets,play_button,stats,sb)

		if stats.game_active:
			ship.update()
			gf.update_bullets(settings,screen,ship,aliens,bullets,stats,sb)
			gf.update_aliens(settings,stats,screen,ship,aliens,bullets,sb)

		gf.update_screen(settings,stats,screen,ship,bullets,aliens,play_button,sb)

run_game()