# -*- coding: utf-8 -*-
def deco(C):
    print("Внутри декоратора")
    return C
@deco
class MyClass:
    def __init__(self, x):
        self.v = x
c = MyClass(5)
print(c.v)
input()
