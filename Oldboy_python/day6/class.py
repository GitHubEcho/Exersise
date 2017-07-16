#!/usr/bin/env python3
#coding:utf-8

"""面向对象(oop)
    主要解决两个问题:
     - 避免重复造轮子
     - 代码的可扩展性

实例变量:存储一个实例的属性,返回地址类
    类变量:共享公用属性,节省了开销

构造函数:实例化一个对象
    析构函数:对象销毁时的操作,无需调用

私有方法:
    类的内部能修改,外部不能,只有通过内部函数进行修改

1.封装
2.继承
3.多态
封装可以隐藏实现细节,使代码模块化

继承可以扩展已存在的代码模块;他们的目的都是为了--->代码的重用

而多态实现可另一个目的---->接口重用

同一种接口,多种实现方式

"""

class student:
    n = 1
    list = []
    def __init__(self,name,age,sex,money = 100):
        self.__name = name
        self.age = age
        self.sex = sex
        self.money = money

    def __del__(self):
        print('%s done !' % self.__name)

    def get(self):
        return self.__name, self.age

    def eating(self):
        print('% eate things' % self.__name)

    def dinking(self):
        print('% dink water' % self.__name)

A = student('heqian',20,'man') #IndentationError: unindent does not match any outer indentation level
print(A)
A.n = 2
A.list.append(A.n)
print(A.n,A.list)
A.get()

B = student('xiaoxiao',21,'man')
B.n = 30
B.list.append(B.n)
print(B.age,B.n,B.list)

print(student.list)

print(A.get())

