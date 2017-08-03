#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

start_time = time.time()
for x in range(1001):
    for y in range(1001):
        for z in range(1001):
            if x*x + y*y == z*z and x + y + z == 1000 :
                print(x,y,z)
runing_time = time.time() - start_time()
print('runing time:%s', runing_time)

start_time = time.time()
for x in range(1001):
    for y in range(1001):
        z = 1000-x-y
        if x*x + y*y == z*z  :
            print(x,y,z)
runing_time = time.time() - start_time
print('runing time:', runing_time)
