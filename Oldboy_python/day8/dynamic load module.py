#!/usr/bin/env python3
#coding:utf-8

lib = __import__('lib.aa')              #导入lib层
print (lib)
A = lib.aa.A()#实例化A对象
print(A.get_name())


import importlib
aa = importlib.import_module('lib.aa')  #导入aa模块
print(aa)
B = aa.A()#实例化B对象
print(B.get_name())

'''
__import__方法是解释器执行代码时使用的方法，官方不推荐使用
importlib
'''