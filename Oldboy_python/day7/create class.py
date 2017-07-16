#!/usr/bin/env python3
#coding:utf-8

# ###通过一般方法构建#############
class people(object):
    def __init__(self):
        self.name = 'heqian'

    def func(self):
        print('hello heqian')

A = people()
A.func()


# #########通过type构建###########
def __init__(self):
    self.name = 'xiaoxiao'

def func(self):
    print('hello xiaoxiao')

people = type('people', (object,), {'func': func,'__init__':__init__})
#type第一个参数：类名
#type第二个参数：当前类的基类
#type第三个参数：类的成员

B = people()
print(B.name)
B.func()

'''


'''