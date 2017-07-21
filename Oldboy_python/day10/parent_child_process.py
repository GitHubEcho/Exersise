#!/usr/bin/env python3
#coding:utf-8

import multiprocessing
import os

def print_info():
    print('\n### current process is ',__name__)
    print('parent process PID:',os.getppid())
    print('current process PID:',os.getpid())


if __name__ == '__main__':
    print_info()                                        #编辑器启动一个主进程执行程序
    p = multiprocessing.Process(target=print_info)      #在程序的主进程中启动一个多进程
    p.start()

'''
进程都是由父进程创建
'''