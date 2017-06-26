#!/usr/bin/python2
#coding:utf-8
"""字典筛选"""
from random import randint
dic = {x: randint(60,100) for x in xrange(1,21)}
print dic
print {k: v for k,v in dic.iteritems() if v >= 80}