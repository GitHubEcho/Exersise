#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#列表有序去重
a = "aAsmr3idd4bgs7Dlsf9eAF"

a_list = list(a)  # 转化为列表，并保存元素顺序


set_list = list(set(a_list))  # 去重

set_list.sort(key=a_list.index)

s = ''.join(set_list)
print(s)