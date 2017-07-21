#!/usr/bin/env python3
#coding:utf-8

import multiprocessing
import threading

def thread_run():
    print(threading.get_ident())


def process(n):
    t = threading.Thread(target=thread_run)
    t.start()
    print('job',n)

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=process,args=(i,))
        p.start()