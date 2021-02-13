# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:00:04 2021

@author: Mike
"""

import pygame

class Ship:
    """A Class to manage the ship."""
    
    
    def __init__(self, ai_game):
        
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('../images/ship.bmp')
        self.image.set_colorkey((230,230,230))
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
        