#/usr/bin/env python2
#coding:utf-8

f = open('hello','r',encoding='utf-8')  #注意w模式会重新创建文件，会删除原文件
# f.write('\nworrld!')
# print(f.read())
# print('--------')
# print(f.read())  #指针已到结尾
print(f.readline())
count = 0
for line in f:
    if count == 9:
        print(line)
    count +=1