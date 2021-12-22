# -*- coding: utf-8 -*-
class MyClass:
   def __init__(self):
    self.i = 20
   def __getattribute__(self, attr):
      print("вызывается метод __getattribute__()")
      return object.__getattribute__(self, attr)
c = MyClass()
print(c.i)
input()
