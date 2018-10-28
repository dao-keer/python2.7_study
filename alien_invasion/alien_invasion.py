# -*- encoding: utf-8 -*-
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏
    pygame.init()
    #实例化设置对象
    ai_settings = Settings()
    #创建屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #设置游戏标题
    pygame.display.set_caption(ai_settings.caption)
    #创建飞船
    ship = Ship(screen, ai_settings)
    #创建子弹列表
    bullets = Group()
    #开始游戏的主循环
    while True:
        screen.fill(ai_settings.bg_color)
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        #更新飞船位置
        ship.update()
        #更新子弹位置
        bullets.update()
        for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                        bullets.remove(bullet)
        #更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()