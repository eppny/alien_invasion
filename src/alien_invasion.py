
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
        
        running = True
        
        while running:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False		
                    
            # Redraw the screen
            # self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.background.image, self.background.rect)
            self.ship.blitme()
            
            # Make the most recently drawn screen visible
            pygame.display.flip()
            
        pygame.quit()

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
