#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pygame,time,random
from pygame.locals import *

class Base(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_name)
        self.screen = screen_temp
class BasePlane(Base):
    def __init__(self,screen_temp,x,y,image_name,plane_size):
        super().__init__(screen_temp,x,y,image_name)
        self.bullet_list = []
        self.plane_size = plane_size
        self.plane_down_list = ['./plane/enemy0_down1.png', './plane/enemy0_down2.png',\
                                './plane/enemy0_down3.png', './plane/enemy0_down4.png']
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list: #刷新飞机显示时同时，刷新子弹
            bullet.display()

            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
                if  bullet.judge_hit(self.x,self.y,self.plane_size):
                    for plane_down_imgae in self.plane_down_list:
                        self.image = pygame.image.load(plane_down_imgae)

            # if True :#bullet.judge_hit(self.x,self.y,self.plane_size):
            #     count = 0
            #     if count == 15:
            #         for plane_down_imgae in self.plane_down_list:
            #             self.image = pygame.image.load(plane_down_imgae)
            #             count = 0
            #     count += 1

class Heroplane(BasePlane):
    def __init__(self,screen_temp):
        super().__init__(screen_temp,200,700,"./plane/hero.gif",(100,124))

    def move_left(self):
        self.x -=5
    def move_right(self):
        self.x +=5
    def fire(self):
        bullet = Bullet(self.screen,self.x,self.y)
        self.bullet_list.append(bullet)

class Enemyplane(BasePlane):
    def __init__(self,screen_temp):
        super().__init__(screen_temp,0,0,"./plane/enemy0.png",(51,39))
        self.direction = 'right'
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

class BaseBullet(Base):
    def __init__(self, screen_temp, x, y,image_name):
        super().__init__(screen_temp, x, y, image_name)
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def judge_hit(self,plane_x,plane_y,plane_size):
        if (self.x > plane_x and self.x < plane_x + plane_size[0] )\
        and (self.y > plane_y and self.y < plane_y + plane_size[1]):
            return True
        else:
            return  False

class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        super().__init__(screen_temp,x + 40,y - 20,"./plane/bullet.png")
    def move(self):
        self.y -= 5
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class Bullet1(BaseBullet):
    def __init__(self, screen_temp, x, y):
        super().__init__(screen_temp, x + 25, y + 40, "./plane/bullet1.png")
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
        enemy.fire()  #自动发射子弹
        enemy.move()  #自动移动

        keyboard_contrl(hero)
        time.sleep(0.01)
        pygame.display.update()