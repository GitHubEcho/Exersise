#!/usr/bin/env python3
#coding:utf-8

import time
t = time.time()   #获取当前时间戳
print(t)

g = time.gmtime(t) #转化为元祖
print(g)

s = time.strftime('%Y-%m-%d %H:%M:%S',g)  #
print(s)

print(time.strptime(s,'%Y-%m-%d %H:%M:%S'))

print(time.mktime(g))

