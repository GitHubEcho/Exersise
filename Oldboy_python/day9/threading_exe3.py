#!/usr/bin/env python3
#coding:utf-8

import time,threading

def run(n):
    print('task',n)
    time.sleep(2)

start_time = time.time()

t_jobs = []
for i in range(50):
    t = threading.Thread(target=run,args=(i,))
    t.start()
    t_jobs.append(t)

for x in t_jobs:
    t.join()
    pass

print('all threading is finished'.center(50,'-'))
print('ccurrent_thread',threading.current_thread())
print('threading finish time ',time.time() - start_time)