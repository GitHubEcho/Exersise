#!/usr/bin/env python3
#coding:utf-8

import time,threading
'''
计算使用线程结束时的总时间
'''
sum = 0
def run(n):
    lock.acquire()
    global sum
    sum += 1
    lock.release()

start_time = time.time()

lock = threading.Lock()
t_jobs = []
for i in range(10000):
    t = threading.Thread(target=run,args=(i,))
    t.start()
    t_jobs.append(t)

for x in t_jobs:
    t.join()


print('all threading is finished'.center(50,'-'))
print('ccurrent_thread',threading.current_thread(),'active_thread',threading.active_count())
print('threading finish time ',time.time() - start_time,sum)