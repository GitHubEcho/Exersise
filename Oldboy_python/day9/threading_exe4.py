#!/usr/bin/env python3
#coding:utf-8

import time,threading
'''
把子线程变成守护进程，程序不用等待线程执行完毕而结束
'''
def run(n):
    print('task',n)
    time.sleep(2)

start_time = time.time()


for i in range(50):
    t = threading.Thread(target=run,args=(i,))
    t.setDaemon(True)
    t.start()



print('all threading is finished'.center(50,'-'))
print('ccurrent_thread',threading.current_thread(),'active_thread',threading.active_count())
print('threading finish time ',time.time() - start_time)