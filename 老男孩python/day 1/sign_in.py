#!/usr/bin/env python2
#coding:utf-8

"""
登录接口
思路：
 1.用户登录时查询登录文件是否密码输入正确
 2.用户输入密码错误三次时，加入黑名单（文件夹）

"""

def sign_in(user,password):
    if username in passwd[0]:
        u = passwd[0].index(username)
        if password == (passwd[1][u]):
            print "登录成功！"
            return 1
        else:
            print "密码错误！"
            return 0
    else:
        print "用户名错误！"
        return 0

def verify():
    users = []
    passwds = []
    f =  open('passwd','r')
    lines = f.readlines() #读入文件的一行并返回元祖
    for data in lines:
        data = data.encode()
        user,passwd = data.split(',')
        user = user.strip() # 使用输入方法read() 或者 readlines() 从文件中读取行时，python并不会删除行结尾符。
        passwd = passwd.strip()
        users.append(user)
        passwds.append(passwd)
        #print users
        #print passwds
    f.close()
    return users,passwds


if __name__ == '__main__':
    username = raw_input("your name :")
    password = raw_input("your passwd:")
    # sign_in(username,pw)
    passwd = verify()
    for x in xrange(2):
        a = sign_in(username, password)
        if a != 0 :
            break
        else:
            print "请再次重新输入"
            username = raw_input("your name :")
            password = raw_input("your passwd:")


