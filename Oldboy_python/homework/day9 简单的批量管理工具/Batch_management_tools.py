#!/usr/bin/env python3
#coding:utf-8

import pickle,os,paramiko,threading,re


def SSH(command,hostname,username,password):
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname= hostname, port=22, username=username, password=password)
        print('\033[32;0m host %s runing result\033[0m'.center(40, '-') % hostname)
        stdin, stdout, stdrr = ssh.exec_command(command)

        res, err = stdout.read(), stdrr.read()
        result = res if res else err
        print(result.decode())
        ssh.close()
    except Exception as e:
        print('\033[31;1m time out! %s error is %s\033[0m' % (hostname,e))

def SFTP(command,hostname,username,password):
    transport = paramiko.Transport((hostname, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    command_list = re.split(' ',command)
    print(command_list)
    if 'put' == command_list[0]:
        sftp.put(command_list[1], command_list[2])

    if 'get' == command_list[0]:
        sftp.get(command_list[1], command_list[2])
    print('\033[32;0mfile transfer success\033[0m')
    transport.close()

def print_group(choose_group):
    '''打印组的字典的第一个值，即主机IP'''
    filename = 'hostgroup/'+choose_group
    #print(filename)
    with open(filename,'rb') as f :
        dic = pickle.load(f)
    print('%s'.center(40, '-') % choose_group)
    host_list = []
    for key in dic.keys():
        print(key)
        host_list.append(key)
    return dic,host_list

if __name__ == '__main__':
    group  = os.listdir('hostgroup')
    for index,x in enumerate(group):
        print(index,x)

    group_index = int(input('please input your choose group index: ').strip())
    choose_group = group[group_index]

    choose_group,host_list  = print_group(choose_group)
    #print(choose_group)
    #print(host_list)
    operating = int(input('you want to "1.Excuting an order"or"2.Transfer file": '))
    if operating == 1:
        #SSH('df','192.168.1.141','root','8520')
        command = input('please input command: ').strip()
        for host in host_list:
            t = threading.Thread(target=SSH,args=(command,host,choose_group[host][0],choose_group[host][1]))
            t.start()

    if operating == 2:
        # SSH('df','192.168.1.141','root','8520')
        command = input('please input command: ').strip()
        for host in host_list:
            t = threading.Thread(target=SFTP, args=(command, host, choose_group[host][0], choose_group[host][1]))
            t.start()




