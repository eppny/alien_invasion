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
        
        self.settings = ai_game.settings
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('../images/ship.bmp')
        self.image.set_colorkey((230,230,230))
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y = self.rect.y - 10
        
        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        self.rect.x = self.x
        
    def center_ship(self): 
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        