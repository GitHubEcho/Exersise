#!/usr/bin/env python3
#coding:utf-8
import os,re,sys

#从磁盘读取文件到内存
conf = "haproxy.cfg"
conf_new = "haproxy.cfg.new"
backend_list = []
server_dict = {}
show_dict = {}
backend_name_dict = {}
server_info = []
server_flag = False  ###初始化server判断标志位###




def new():
    pass

def search():
    with open('haproxy.cfg','r') as f:
        for line in f:
            line = line.strip('\n')
            # if 'backend' in line:
            if  re.match('backend',line):
                print(line)
                backend_name = re.split('\s+', line)[1]
                backend_list.append(backend_name)
            elif re.match('\s+server',line):
                print(line)
                server_info = re.split('\s+',line)
                server_info.append(server_info)
                print(server_info)


search()


def delete():
    pass

# list = ['NEW','SEA','DEL']
# for x in list:
#     print('{lis}:{operating}'.format(lis = list.index(x)+1,operating = x))
# while True:
#     index = input('input your index:')
#     if index.isdigit():
#         index = int(index)
#         if index >len(list) and index < 0:
#             print('error')
#         else:
#             if index == 1:
#                 pass
#             elif index == 2:
#                 search()
#                 pass
#             else:
#                 pass
#     else:
#         print('option invalid')