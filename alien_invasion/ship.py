# -*- encoding: utf-8 -*-
import pygame

class Ship(object):
    def __init__(self, screen, ai_settings):
        #初始化飞船所在的屏幕
        self.screen = screen
        self.ai_settings = ai_settings
        #初始化飞船的图片，和图片本身的大小
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #将飞船定位到屏幕的底部中央位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #持续向右移动标识
        self.moving_right = False
        #持续向左移动标识
        self.moving_left = False
        #飞船的x轴位置
        self.centerx = self.rect.centerx
    
    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.centerx -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx