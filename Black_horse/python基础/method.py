#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class Animal(object):
    def foo(self,x):
        print(self,x)

    @staticmethod
    def static_foo(x):
        print(x)

    @classmethod
    def class_foo(cls,x):
        print(cls,x)
a = Animal()
a.foo(1)
Animal.static_foo(1)
Animal.class_foo(1)
