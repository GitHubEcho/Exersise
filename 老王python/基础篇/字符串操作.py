#!/usr/bin/env python2
#coding:utf-8
import string
"""
字符串操作

"""
#replace()方法 按所给的字符串整体替换
a = "I am lilei" #注意字符串为不可变对象，修改后需要赋值

a.replace('lilei','echo')  #注意替换需按续进行

#translate()方法 读取翻译表，一一对应替换，无序且需要相同的长度
a = "3211231231"

#生成翻译表
t = string.maketrans('123','abc') #一一对应替换，无顺序，所以需要有相同的长度

print (a.translate(t))
print (a.translate(t,'1'))#'1'代表要删除的字符串，逐字删除