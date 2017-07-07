#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import os


# 根据标题获取配置信息
def fetch(backend):
    backend_title = 'backend %s' % backend
    record_list = []
    with open('ha') as obj:
        flag = False
        for line in obj:
            line = line.strip()
            if line == backend_title:
                flag = True
                continue
            if flag and line.startswith('backend'):
                flag = False
                break
            if flag and line:
                record_list.append(line)

    return record_list




# 在指定标题下插入配置信息
def insert(dict_data):
    backend = dict_data.get('backend')
    backend_title = "backend %s" % backend
    content = "server %s %s weight %d maxconn %d" % (
    dict_data['record']['server'], dict_data['record']['server'], dict_data['record']['weight'],
    dict_data['record']['maxconn'])
    record_list = fetch(backend)
    flag = True
    count = 0
    if not record_list:
        record_list.append(backend_title)
        record_list.append(content)
        with open('conf.txt', 'r') as read_file, open('conf.txt.bak', 'w') as write_file:
            for line in read_file:
                write_file.write(line)
            for l in record_list:
                if l.startswith("backend"):
                    write_file.write(l + '\n')
                else:
                    write_file.write(" " * 8 + l)
    else:
        record_list.append(content)
        with open('conf.txt', 'r') as read_file, open('conf.txt.bak', 'w') as write_file:
            for line in read_file:
                if flag:
                    write_file.write(line)
                    if line.startswith(backend_title):
                        for l in record_list:
                            write_file.write(" " * 8 + l + '\n')
                        flag = False
                else:
                    count = count + 1
                    if (count == record_list.__len__() - 1):
                        flag = True
    os.rename('conf.txt.bak', 'conf.bak')
    os.rename('conf.bak', 'conf.txt')


# 删除指定标题的信息
def delete(dict_data):
    backend = dict_data.get('backend')
    backend_title = "backend %s" % backend
    content = "server %s %s weight %d maxconn %d" % (
    dict_data['record']['server'], dict_data['record']['server'], dict_data['record']['weight'],
    dict_data['record']['maxconn'])
    record_list = fetch(backend)
    content = content.strip()
    print(content)
    if not record_list:
        return
    else:
        if record_list.__contains__(content):
            return
        else:
            print(record_list)
            record_list.__delattr__(record_list.index(content))
            with open('conf.txt', 'r') as read_file, open('conf.txt.bak', 'w') as write_file:
                for line in read_file:
                    if flag:
                        write_file.write(line)
                        if line.startswith(backend_title):
                            for l in record_list:
                                write_file.write(" " * 8 + l + '\n')
                            flag = False
                    else:
                        count = count + 1
                        if (count == record_list.__len__() + 1):
                            flag = True
    os.rename('conf.txt.bak', 'conf.bak')
    os.rename('conf.bak', 'conf.txt')


if __name__ == '__main__':
    print('1、获取；2、添加；3、删除')
    num = input('请输入序号：')
    data = input('请输入内容：')
    if num == '1':
        print(fetch(data))
    else:
        dict_data = json.loads(data)
        if num == '2':
            insert(dict_data)
        elif num == '3':
            delete(dict_data)
        else:
            pass
            # data = "www.oldboy.org"
            # fetch(data)
            # data = '{"backend": "www.oldboy.com","record":{"server": "100.1.7.90","weight": 20,"maxconn": 31}}'
            # dict_data = json.loads(data)
            # add(dict_data)
            # remove(dict_data)
