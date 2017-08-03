#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def extend_list(val,list = []):
    list.append(val)
    return list

list1 = extend_list(10)
list2 = extend_list(123, ['a', 'b', 'c'])
list3 = extend_list('a')

print('list1:',list1)
print('list2:',list2)
print('list3:',list3)

print(hex(id(list1)))
print(hex(id(list2)))
print(hex(id(list3)))
