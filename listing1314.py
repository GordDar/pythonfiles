# -*- coding: utf-8 -*-
class MyClass:
   def __init__(self):
     self.x = 50
     self.arr = [1,2,3]
   def __eq__(self, y):
       return self.x ==y
   def __contains__(self, y):
       return y in self.arr 
c = MyClass()
print("ok" if c == 50 else "ne ok")
print("ok" if c == 51 else "ne ok")
print("est" if 5 in c else "nety")
input()
