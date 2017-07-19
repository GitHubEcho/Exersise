#!/usr/bin/env python3
#coding:utf-8
with open('test.xml') as f:
    print(f.readlines())
    lines_ = f.readlines()
    print(type(lines_))

    lines = (line.strip() for line in f)
    print(type(lines))
    for line in lines:
         print(line)

'''
readline读取文件的一行，注意有文件的游标
lines是一个generater
lines_是一个list

'''