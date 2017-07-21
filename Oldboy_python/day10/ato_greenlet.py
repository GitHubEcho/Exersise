#!/usr/bin/env python3
#coding:utf-8

import gevent,time
start_time = time.time()

def func1():
    print('fun1 start ...')
    gevent.sleep(3)
    print('fun1 end...')


def func2():
    print('fun2 start ...')
    gevent.sleep(2)
    print('fun2 end...')


def func3():
    print('fun3 start ...')
    gevent.sleep(1)
    print('fun3 end...')

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3)
])
print(time.time()-start_time)