#!/usr/bin/env python3
#coding:utf-8


#class People:
class People(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print('%s done !' % self.name)

    def get(self):
        return self.name, self.age

    def eating(self):
        print('% eate things' % self.name)

    def dinking(self):
        print('% dink water' % self.name)

class relationship(object):
    def __init__(self,n1,n2,n3):
        pass
    def makefriends(self,obj):
        print('%s make a friend %s'%(self.name,obj.name))


class Man(People,relationship):
    # def __init__(self,name,age,sex,money = 100):
    #     #People.__init__(self,name,age,sex)
    #     super(Man,self).__init__(name,age,sex)
    #     self.money = 200
    pass

class Woman(People):
     def __init__(self,name,age,sex='woman'):
         #如果选择构造对象,不能只构造一部分属性
         super(Woman,self).__init__(name,age,sex)
         self.sex = 'woman'



A = Man('heqian',20,'man')
print(A.sex)

B = Woman("xiaoxiao",23,'woman')
A.makefriends(B)



