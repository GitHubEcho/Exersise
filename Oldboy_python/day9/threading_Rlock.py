#!/usr/bin/env python3
#coding:utf-8

import threading,time


def run(n):
    semaphroe.acquire()
    time.sleep(1)
    print('thread' ,n)
    semaphroe.release()

if __name__ == '__main__':
    semaphroe = threading.BoundedSemaphore(5)
    for i in range(20):
        t =threading.Thread(target=run,args=(i,))
        t.start()
print(threading.current_thread())
while threading.current_thread() != 1:

    pass
else:
    print('all threads is done '.center(60,'-'))
