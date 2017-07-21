#!/usr/bin/env python3
#coding:utf-8
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    print('hello world', i)
    l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f, args=(lock, num)).start()

'''
共享屏幕资源，在输出时可能会乱，可以在linux上试试
'''