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
    print e
