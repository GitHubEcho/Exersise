#!/usr/bin/env python3
# coding:utf-8

import time

fmt = '{m:3d} [{s:<20}]'.format


def progressbar():
    for n in range(21):
        time.sleep(0.1)
        print (fmt(m = n * 5, s ='=' * n))  #print('{:3d} [{:<20}]'.format(n * 5, '=' * n))

progressbar()

'''
format它通过{}和:来代替%(冒号前面是名称，如不写，默认为位置)
python中函数可以赋值给变量后再调用
'''