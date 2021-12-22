# -*- coding: utf-8 -*-
class MyClass:
    def __init__(self, x):
        self.__Var = x
    def set_Var(self, x):
        self.__Var = x
    def get_Var(self):
        return self.__Var
c = MyClass(10)
print(c.get_Var())
c.set_Var(20)
print(c.get_Var())
try:
    print(c.__Var)
except AttributeError as msg:
    print(msg)
c._MyClass__Var = 50
print(c.get_Var())
input()
