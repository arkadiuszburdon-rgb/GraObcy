import sys
import pygame
from com.vncs.python.aliengame.settings import Settings
from com.vncs.python.aliengame.ship import Ship

class AlienInvasion:
    """A class to manage the game assets and behavior. """
    
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # Ustawienia ekranu pełnoekranowego lub okna

        if(self.settings.fullscreen):
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_width()
            self.settings.screen_height = self.screen.get_height()
        else:
            self.screen = pygame.display.set_mode(( self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)  # Create an instance of Ship

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.update()
        self.ship.blitme()  # Draw the ship
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting game.")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
                    #print(f"Right arrow pressed: {self.ship.rect.midbottom}")
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                    #print(f"Left arrow pressed: {self.ship.rect.midbottom}")
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            print("Exiting game.")
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

   
                    