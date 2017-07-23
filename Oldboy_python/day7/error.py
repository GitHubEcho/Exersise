#!/usr/bin/env python3
#coding:utf-8
class Exception(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):        #类名调用打印信息
        return self.message


try:
    raise Exception('我的异常')  #raise触发异常
except Exception as e:
    print (e)

#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    1 / 0
except Exception as e:
    '''异常的父类，可以捕获所有的异常'''
    print ("0不能被除")
else:
    '''保护不抛出异常的代码'''
    print ("没有异常")
finally:
    print ("最后总是要执行我")