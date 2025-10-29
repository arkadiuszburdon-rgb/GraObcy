import sys
import pygame
from com.vncs.python.aliengame.settings import Settings
from com.vncs.python.aliengame.ship import Ship

class AlienInvasion:
    """A class to manage the game assets and behavior. """
    
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings()
        self.ship = Ship(self)  # Create an instance of Ship

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # Draw the ship
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting game.")
                sys.exit()