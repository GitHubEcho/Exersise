#!/usr/bin/env python3
#coding:utf-8


class animal :
    name = 'xiaohe'
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.__age = age

    @staticmethod
    def eat(self):  #注意self的颜色
        print('%s is eating '%self.name)

    @property
    def drink(self):
        print('%s is drinking '%self.name)

    @drink.setter
    def drink(self,status):
        print('%s is setted '%status)

    @drink.deleter
    def drink(self):
        print('drink is deleted')

    @classmethod
    def sleep(cls):
        print('%s is sleeping '%cls.name)

A = animal('xiaoxiao','cat',5)

A.eat(A)
A.drink = 'heqian'
A.drink
del A.drink
A.drink
A.sleep()



"""静态方法
@staticmethod
和类解除关系，但是要通过类名，来调用


属性方法
@property
把一个方法变成一个静态属性
@eat.seter
@eat.deleter
"""


