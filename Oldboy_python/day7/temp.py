
#!/usr/bin/env python3
#coding:utf-8

class Dog(object):
    def __init__(self, name):
        self.name = name

    # @classmethod
    # def eat(self):
    #     print("%s is eating" % self.name)

    @classmethod
    def drink(self):
        print('%s is dinking '%self.name)


d = Dog("ChenRonghua")
d.name
d.eat()