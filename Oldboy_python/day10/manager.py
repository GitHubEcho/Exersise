#!/usr/bin/env python3
#coding:utf-8

import os
from multiprocessing import Manager,Process

def f(dic,list):
    dic[os.getpid()] = os.getpid()
    list.append(os.getpid())
    print(dic)
    print(list)

if __name__ == '__main__':
    with Manager() as Manager:
        dic = Manager.dict()
        list = Manager.list()

        p_list = []

        for _ in range(5):
            p = Process(target=f,args=(dic,list))
            p.start()
            p_list.append(p)

        for x in p_list:
            x.join()

