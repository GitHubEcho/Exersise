#!/usr/bin/env python3
#coding:utf-8

import threading,time

def run(n):
    print('task ',n)
    time.sleep(1)
t1 = threading.Thread(target=run,args=('t1',))
t2 = threading.Thread(target=run,args=('t2',))
t1.start()
t2.start()


run(1)
run(2)