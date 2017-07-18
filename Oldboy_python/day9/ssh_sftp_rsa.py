#!/usr/bin/env python3
#coding:utf-8

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa_2048.pub')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.1.141', port=22, username='root', pkey=private_key)

stdin,stdout,stdrr = ssh.exec_command('top')

res,err = stdout.read(),stdrr.read()

result = res if res else err
print(result.decode())

ssh.close()