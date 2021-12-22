# -*- coding: utf-8 -*-
class MyClass:
    pass
MyClass.x = 10
c1, c2 = MyClass(), MyClass()
c1.y = 10
c2.y = 20
print(c1.x, c1.y)
print(c2.x, c2.y)
input()
