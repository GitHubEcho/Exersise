#!/usr/bin/env python3
#coding:utf-8

import json

dic = {"group1": {"192.168.1.141": {"password": "8520", "username": "root", "port": 22}, "192.168.20.219": {"password": "zyw@123", "username": "root", "port": 22}}, "group2": {"192.168.20.217": {"password": "123456", "username": "root", "port": 22}}}

with open('database','w') as f:
    json.dump(dic,f)