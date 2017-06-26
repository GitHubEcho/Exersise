#!/usr/bin/env python2
#coding:utf-8

"""set fliter"""
from random import randint
data = [randint(-10,10) for _ in xrange(10)]
s = set(data)
print {x for x in s if x%3==0}
