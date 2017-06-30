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
        print "用户名不存在！"
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

def blacklist():
    users = []
    f = open('blacklist','r')
    lines = f.readlines()
    for data in lines :
        data = data.encode()
        user = data
        user = user.strip()
        users.append(user)
    f.close()
    return users

if __name__ == '__main__':
    passwd = verify()
    blacklist = blacklist()
    #print blacklist
    count = 0
    while count < 3:
        username = raw_input("your name :")
        password = raw_input("your passwd:")
        if username in blacklist:
            print '用户已被锁定，请解绑后登录'
            break
        else:
            a = sign_in(username, password)
            if a != 0 :
                break
            elif count == 2:
                print '输入超过三次，用户已被锁定'
                a = open('blacklist','rw')
                a.write('username')
                a.close()
            else:
                print "请再次重新输入"
        count += 1




