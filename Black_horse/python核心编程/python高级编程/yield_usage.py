#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def fib(sum):
    a,b = 0,1
    for _ in range(sum):
        res = yield b
        a,b =b ,a+b
        print(res)

f = fib(10)

f.send(None)  #执行一次__next__(),从上一次yield停止的表达式传值
f.send('hh')

'''
开始就使用生成器的方法:
①先f.__next__()
②先send(None)
'''