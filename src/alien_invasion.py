
import sys
import pygame

from settings import Settings
from ship import Ship
from background import Background

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        
        self.settings = Settings()
        
        self.background = Background("../images/background.jpg", [0,0])
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
    def run_game(self):
        """Start the main loop for the game"""
        
        self.running = True
        
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
        pygame.quit()
        
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
                
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.background.image, self.background.rect)
        self.ship.blitme()
        
        pygame.display.flip()
        
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
