#!/usr/bin/env python3
#coding:utf-8

import time ,threading

flag = threading.Event()

def lighter():
    count = 0
    flag.set()
    while True:
        if count > 5 and count < 10:
            print('\033[41;1mred lighter on \033[0m')
            flag.clear()  #标志位清零变红灯
        elif count > 10 :
            flag.set()
            count = 0
        else:
            print('\033[42;1mgreen lighter on \033[0m')
        count += 1
        time.sleep(1)

def car(n):
    while True:
        if flag.is_set():
            print('[%s] is passing...'%n)
        else:
            flag.wait()
            print('[%s] is waiting...'%n)
        time.sleep(1)


car1 = threading.Thread(target=car,args = (1,))
car1.start()

lighter = threading.Thread(target=lighter)
lighter.start()