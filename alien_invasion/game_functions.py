# -*- encoding: utf-8 -*-
import pygame
import sys

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            #飞船右移
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            #飞船左移
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            #飞船停止右移
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            #飞船停止左移
            if event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ship):
    #加载飞船的位置
    ship.blitme()
    #绘制最新的屏幕信息
    pygame.display.flip()
