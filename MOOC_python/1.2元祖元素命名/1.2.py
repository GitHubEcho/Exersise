#!/usr/bin/env python2
#coding:utf-8
from collections import namedtuple
"""
元祖的形式存储，但是空间中存在大量的索引值,不易于阅读

"""
# ('jim',16,'male','1187984211@qq.com')
# ('tom',18,'female','464009025@qq.com')
student = ('jim',16,'male','1187984211@qq.com')

#name
print student[0]

#age
print student[1]

'''
//C语言解决办法

①宏定 义
#define NAME 0
#define AGE 1

②枚举
enum Student{
    NAME,
    AGE,
    SEX,
}
1.在python中没有枚举，但是用类似枚举的方法
2.使用标准库中collections.namedtuple替代内置的tuple
'''
#方案一
# NAME = 0
# AGE = 1
# SEX = 3

NAME,AGE,SEX,EMAIL = xrange(4)
#name
print student[NAME]

#age
print student[AGE]

#方案二
student = namedtuple('Student',['NAME','AGE','SEX','EMAIL'])
s = student('jim',16,'male','1187984211@qq.com')
print s.NAME








