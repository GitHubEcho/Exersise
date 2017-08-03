# /usr/bin/python3
# -*- coding:utf-8 -*-

def fib(sum):
    a,b = 0,1
    for _ in range(sum):
        a,b = b,a+b
        yield a  #①停止函数 ②返回yield后面的值

f = fib(10)  #生成一个生成器

next(f)