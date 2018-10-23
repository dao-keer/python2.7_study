# -*- encoding: utf-8 -*-
import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    #初始化游戏
    pygame.init()
    #实例化设置对象
    ai_settings = Settings()
    #创建屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen.fill(ai_settings.bg_color)
    #设置游戏标题
    pygame.display.set_caption(ai_settings.caption)
    #创建飞船
    ship = Ship(screen)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        #加载飞船的位置
        ship.blitme()
        #绘制最新的屏幕信息
        pygame.display.flip()

run_game()