#/usr/bin/env python2
#coding:utf-8

f = open('hello','r+',encoding='utf-8')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
print(f.seek(10))
print(f.write('hhh'))
print(f.readline())
print(f.readline())
print(f.tell())