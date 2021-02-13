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
