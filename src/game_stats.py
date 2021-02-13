# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 13:43:59 2021

@author: Mike
"""

class GameStats:
    """Ttack statistics for Alien Invasion"""
    
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.game_active = False
        