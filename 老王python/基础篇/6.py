#!/usr/bin/env python2
#coding:utf-8

"""
格式化输出
"""
print '%s fruit is %s' % ('my','apple')
print '{} fruit is {}'.format('my','apple')
print '{1} fruit is {0}'.format('my','apple')
print '{who} fruit is {fruit}'.format(who = 'my',fruit = 'apple')
print '%(who)s fruit is %(fruit)s'%{'who':'my','fruit':'apple'}

"""
文件操作
"""
a = open('test','w')
a.write('my name is heiqian')
a.close()

a = open('test','r')
a.read()
a.read(500)
a.seek(0)
a.close()

"""
字符串不可变，dic，list可变
"""


