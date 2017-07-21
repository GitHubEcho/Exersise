#!/usr/bin/env python3
#coding:utf-8

from  greenlet import greenlet

def func1():
    print(12)
    t2.switch()
    print(56)
    t2.switch()

def func2():
    print(98)
    t1.switch()
    print(55)
    t2.switch()

t1 = greenlet(func1)
t2 = greenlet(func2)  #定义了两个切换器
t1.switch()