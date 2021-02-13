# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:53:37 2021

@author: Mike
"""

import pygame
from pygame.sprite  import Sprite

class Alien(Sprite):
    """A class to represent a single alien"""
    
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        
        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("../images/alien.bmp")
        self.image.set_colorkey((230,230,230))
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)