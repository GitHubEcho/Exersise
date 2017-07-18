#!/usr/bin/env python3
#coding:utf-8

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.1.141',port=22,username='root',password='8520')

stdin,stdout,stdrr = ssh.exec_command('top')

res,err = stdout.read(),stdrr.read()

result = res if res else err
print(result.decode())

ssh.close()