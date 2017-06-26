#!/usr/bin/python2
#coding:utf-8
"""列表中筛选数据"""
from random import randint
data = [randint(-10,10)for _ in xrange(10)]
print(data)

#fliter函数筛选
print filter(lambda x:x >= 0,data)


#列表过滤
print [x for x in data if x >= 0]


"""note:
# 1.lambda 会创建一个函数对象，，但是不会把函数的对对象赋值给标识符，儿def则会把函数对象赋值给一个变量。
# 2.lambda 是一个表达式，而def是一个语句。
"""

