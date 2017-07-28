#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pygame,time,random
from pygame.locals import *

class Heroplane(object):
    def __init__(self,screen_temp):
        self.x = 230
        self.y = 700
        self.image = pygame.image.load("./plane/hero.gif")
        self.screen = screen_temp
        self.bullet_list = []
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
    def move_left(self):
        self.x -=5
    def move_right(self):
        self.x +=5
    def fire(self):
        bullet = Bullet(self.screen,self.x,self.y)
        self.bullet_list.append(bullet)
class Enemyplane(object):
    def __init__(self,screen_temp):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("./plane/enemy-1.gif")
        self.screen = screen_temp
        self.bullet_list = []
        self.direction = 'right'

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        self.fire()
        for bullet in self.bullet_list:  #刷新飞机显示时同时，刷新子弹
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
    def move(self):
        if self.direction == 'right':
            self.x -= 3
        elif self.direction == 'left':
            self.x += 3
        if self.x > 430:
            self.direction = 'right'
        elif self.x < 0:
            self.direction = 'left'
    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 25 or random_num == 75:
            bullet = Bullet1(self.screen,self.x,self.y)
            self.bullet_list.append(bullet)
class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x + 40
        self.y = y - 20
        self.image = pygame.image.load("./plane/bullet.png")
        self.screen = screen_temp
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y -= 5
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False
class Bullet1(object):
    def __init__(self,screen_temp,x,y):
        self.x = x + 25
        self.y = y + 40
        self.image = pygame.image.load("./plane/bullet1.png")
        self.screen = screen_temp
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y += 5
    def judge(self):
        if self.y > 852:
            return True
        else:
            return False
def keyboard_contrl(plane_temp):
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
                plane_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                plane_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                plane_temp.fire()

if __name__ == "__main__":

    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,890),0,32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./plane/background.png").convert()

    #创建战机
    hero = Heroplane(screen)
    #创建敌机
    enemy = Enemyplane(screen)
    #3. 把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        keyboard_contrl(hero)
        time.sleep(0.01)
        pygame.display.update()