# -*- encoding: utf-8 -*-
import pygame
import sys
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    #飞船右移
    if event.key == pygame.K_RIGHT:
        print 'rrrrrrrrrrrrr'
        ship.moving_right = True
    #飞船左移
    if event.key == pygame.K_LEFT:
        print 'lllllllllllll'
        ship.moving_left = True
    
    if event.key == pygame.K_UP:
        print 'sssssssssssss'
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    #飞船停止右移
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    #飞船停止左移
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
    #绘制所有子弹
    for bullet in bullets:
        bullet.draw_bullet()
    #加载飞船的位置
    ship.blitme()
    #绘制最新的屏幕信息
    pygame.display.flip()
