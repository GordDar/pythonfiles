# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta
class MyClass(metaclass=ABCMeta):
   @abstractmethod
   def func(self, x):
     pass 
class Class2(MyClass):
    def func(self, x):
        print(x)
class Class3(MyClass):
    pass
c2 = Class2()
c2.func(50)
c3 = Class3()
try:
    c3.func(50)
except TypeError as msg:
    print(msg)
input()
