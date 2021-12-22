# -*- coding: utf-8 -*-
class MyClass:
    @classmethod
    def func(cls, x):
       print(cls,x)
MyClass.func(10)
c = MyClass()
c.func(50)
input()
