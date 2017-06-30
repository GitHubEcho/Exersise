#!/usr/bin/env python2
#coding:utf-8

"""
登录接口
思路：
 1.用户登录时查询登录文件是否密码输入正确
 2.用户输入密码错误三次时，加入黑名单（文件夹）

"""

def sign_in(user,passwd):
#    if user in s and passwd in s:
    pass

def verify():
    users = []
    passwds = []
    with open(passwd,'r') as  f:
        pw = f.readline()
    users,passwds = pw.split(',')
    return users,passwds


if __name__ == '__main__':
    username = input("your name :")
    passwd = input("your passwd:")
    sign_in(username,passwd)
    print __name__
    print verify()