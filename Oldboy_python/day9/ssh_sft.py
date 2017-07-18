#!/usr/bin/env python3
#coding:utf-8

import paramiko
transport = paramiko.Transport(('192.168.1.141', 22))
transport.connect(username='root', password='8520')
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('ssh.py', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.get('/tmp/test_from_win', 'fromlinux.txt')

transport.close()