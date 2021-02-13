# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:26:01 2021

@author: Mike
"""

import pygame

class Background(pygame.sprite.Sprite):
    
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    