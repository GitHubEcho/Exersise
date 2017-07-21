#!/usr/bin/env python3
#coding:utf-8

from urllib import request
import gevent,time
from gevent import monkey

monkey.patch_all()

urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/' ]

def f(url):
    print('GET:',url)
    res = request.urlopen(url)
    data = res.read()
    print('%s bytes recevied from %s'%(len(data),url))

sync_time = time.time()
for x in urls:
    f(x)
print('同步I/O:',time.time() - sync_time)

async_time = time.time()
gevent.joinall([
    gevent.spawn(f,'https://www.python.org/'),
    gevent.spawn(f,'https://www.yahoo.com/'),
    gevent.spawn(f,'https://github.com/')
])
print("异步cost",time.time() - async_time)