#!/usr/bin/env python3
#coding:utf-8

import shelve

with shelve.open('shelve.data') as f:
    print(f.get('test'))
    print(f.get('time'))
    f.get('test')()
