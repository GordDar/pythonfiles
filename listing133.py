# -*- coding: utf-8 -*-
class MyClass:
    def __init__(self):
        self.x = 10
    def get_x(self):
        return self.x
c = MyClass()
print(getattr(c, "x"))
print(getattr(c, "get_x")())
setattr(c, "y", 12)
print(getattr(c, "y"))
delattr(c, "y")
print(hasattr(c, "y"))
input()
