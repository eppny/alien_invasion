# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 09:36:33 2021

@author: Mike
"""

class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 0.25
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
