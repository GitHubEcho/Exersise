# -*- coding:utf-8 -*-
import os

print('当前进程:%s 启动中 ....' % os.getpid())
pid = os.fork()
if pid == 0:
    print('子进程:%s,父进程是:%s' % (os.getpid(), os.getppid()))
else:
    print('进程:%s 创建了子进程:%s' % (os.getpid(),pid ))

"""

说明：fork函数会返回两次结果，因为操作系统会把当前进程的数据复制一遍，
    然后程序就分两个进程继续运行后面的代码，fork分别在父进程和子进程中返回，
    在子进程返回的值pid永远是0，在父进程返回的是子进程的进程id。
"""