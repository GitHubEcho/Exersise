#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *

if __name__ == "__main__":

    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,890),0,32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./plane/background.png").convert()

    #创建战机
    hero = pygame.image.load("./plane/hero.gif").convert()

    #3. 把背景图片放到窗口中显示
    x = 230
    y = 600
    while True:
        screen.blit(background,(0,0))
        screen.blit(hero, (x, y))
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    x +=5
                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x -=5
                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')
        pygame.display.update()