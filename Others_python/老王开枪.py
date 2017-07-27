#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class Person(object):
    '''人类'''
    def __init__(self,name ):
        self.name = name
        self.qiang = None
        self.hp = 100
    def zhuangzidanjia(self,danjia_temp,zidan_temp):
        '''保存子弹到弹夹中'''
        danjia_temp.baocun(zidan_temp)
    def zhuangdanjia(self,qiang_temp,danjia_temp):
        qiang_temp.zhuangru(danjia_temp)
    def chiqiang(self,qiang_temp):
        self.qiang = qiang_temp
    def attack(self,enemy):
        self.qiang.fire(enemy)
    def diaoxue(self,shanghai):
        self.hp = self.hp - shanghai

    def __str__(self):
        if self.hp:
            return '%s的血量为:%s'%(self.name,self.hp)
        else:
            return '%s 挂了'%self.name

class Qiang(object):
    '''枪类'''
    def __init__(self,name):
        self.name = name
        self.danjia = None
    def zhuangru(self,danjia_temp):
        self.danjia=danjia_temp
    def __str__(self):
        if self.danjia:
            return ('枪的信息：%s，弹夹信息%s'%(self.name,self.danjia))
        else:
            return ('枪没有弹夹')
    def fire(self,enemy):
        # 从弹夹获得一发子弹
        zidan_temp  = self.danjia.tanchu_zidan()
        #伤害别人
        if zidan_temp:
            zidan_temp.dazhong(enemy)
        else:
            print('弹夹没有子弹了')

class Danjia(object):
    '''弹夹类'''
    def __init__(self,size):
        self.size = size
        self.zidan_list = []
    def __str__(self):
        if self.zidan_list:
            return('弹夹信息:%s/%s'%(len(self.zidan_list),self.size))
        else:
            return ('弹夹没子弹了')
    def baocun(self,zidan_temp):
        '''弹夹保存子弹'''
        self.zidan_list.append(zidan_temp)
    def tanchu_zidan(self):
        return self.zidan_list.pop()

class Zidan(object):
    '''子弹类'''
    def __init__(self,shanghai):
        self.shanghai  = shanghai
    def dazhong(self,enemy):
        enemy.diaoxue(self.shanghai)

def main():
    '''主类'''
    laowang = Person('老王')
    AK47 = Qiang('AK47')
    danjia = Danjia(15)
    # 准备有子弹有弹夹的枪,并装入十发子弹
    for x in range(10):
        zidan = Zidan(10)
        laowang.zhuangzidanjia(danjia,zidan)
    laowang.zhuangdanjia(AK47,danjia)
    # 老王持枪
    laowang.chiqiang(AK47)
    # 创建并射击敌人
    laoli = Person('老李')
    print(laoli)
    # 向老李攻击十次老李
    for x in range(10):
        print('第%s次攻击'.center(40,'-')%x)
        print(laowang)
        print(AK47)
        print(danjia)
        laowang.attack(laoli)
        print(laoli)

if __name__ == '__main__':
   main()


