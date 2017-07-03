#coding:utf-8
import copy
a = ['heiqan','liangge','haoge',['HQ','LV'],'wanglun']
b = copy.deepcopy(a) #深copy
print(a)
print(b)
b[0] = 'HQ'
a[3][0] = 'LVS'
print(a)
print(b)

"""深浅copy
浅copy复制的方式:

#调用copy模块
    b = copy.copy(a)
#切片方式
    b = a[:]  先创建b列表，通过迭代a赋值给b
#list()方法
    b = list(a)

浅copy实用性
创建供共享账号
a = ['name',['saving',0]]
heqian = a[:]
heqian[0] = 'heqian'

wife = a[:]
wife[0] = 'wife'

"""
#共享账号
a = ['name',['saving',0]]
heqian = a[:]
heqian[0] = 'heqian'
heqian[1][1] = 50
print heqian

wife = a[:]
wife[0] = 'wife'
print wife