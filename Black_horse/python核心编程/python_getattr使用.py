#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
用python的魔法方法实现
class Foo
print(Foo().think.different.incast)

输出结果：
think different itcast
'''


class Foo(object):
    ''' '''

    def __init__(self):
        pass

    def __getattr__(self, item):  # 属性拦截器
        print(item, end=' ')  # 不换行输出
        return self

    def __getattribute__(self, item): # 定义当通过.去调用属性时，查找的次序
        return self.item # 循环调用

    def __str__(self):  # 调用对象
        return ''

    def foo(self):
        pass
        #print(self)

print(Foo().think.different.incast)
print(Foo().foo())
print(Foo.__dict__)