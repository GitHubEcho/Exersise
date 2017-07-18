#!/usr/bin/env python3
#coding:utf-8
class people:
    pass

class man:
    __meta__ = people
    def __init__(self):
        self.name = 'xiaoxiao'

    def __call__(self, *args, **kwargs): #ython中的可变参数，*args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict
        print(self.name)

B = man()
B()


print(type(B))   #输出<class '__main__.man'>    #指明由man类所创建
print(type(man)) #输出<class 'type'>            #指明由type类所创建

"""
__call__      内建类方法，对象调用时调用此函数
__metaclass__ 类的内建属性，可以表示该类是由谁创建的

"""
