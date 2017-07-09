#!/usr/bin/env python3
#coding:utf-8
import datetime
import shelve

def test():
    print('hello')

name = {'heiqan','xiaoxiao'}

with shelve.open('shelve.data') as f:
    f['name'] = name
    f['test'] = test
    f['time'] = datetime.datetime.now()


# f = shelve.open('shelve.data')
# f['name'] = name
# f['test'] = test
# f['time'] = datetime.datetime.now()

