#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#替换多个字符串
def replace_string(str,oldString,newString):
    #string =''
    str_list = str.split(oldString)
    print(newString.join(str_list))
    # if str.startswith(oldString):
    #     print()
    #     # for s in str_list:
    #     #     string =  newString + s
    #     # print(string)
    # elif  str.endswith(oldString):
    #     for x in str_list:
    #         string = string + x + newString
    #     print(string)
    # else:
    #     print(newString.jion(str_list))
        # for i in range(len(str_list)-1):
        #     string = str_list[i]+newString+str_list[i+1]
        # print(string)

replace_string('World Hello World!','World','Tom')