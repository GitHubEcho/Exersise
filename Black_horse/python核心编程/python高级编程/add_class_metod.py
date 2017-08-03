#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import types

class Test(object):
    def __init__(self,new_name ):        self.name = new_name

def run(self):
    print('%s is runing '%self.name)


#添加类属性
t = Test('xiaoxiao')
t.age = 20
print(t.age)

#添加类方法
t.run = types.MethodType(run,t)
xxx = types.MethodType(run,t)   #表明名字只是指向
xxx()
t.run()         #最好名字相同，好理解

