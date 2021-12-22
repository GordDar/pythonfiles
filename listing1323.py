# -*- coding: utf-8 -*-
class MyClass:
    def __init__(self, x):
        self.__Var = x
    @property
    def v(self):
        return self.__Var
    @v.setter
    def v(self, x):
        self.__Var = x
    @v.deleter
    def v(self):
        del self.__Var
c = MyClass(10)
print(c.v)
c.v = 20
print(c.v)
del c.v
input()
