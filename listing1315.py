# -*- coding: utf-8 -*-
class MyClass:
    @staticmethod
    def func1(x, y):
       return x+y
    def func2(self, x, y):
        return x+y
    def func3(self, x, y):
        return MyClass.func1(x,y)
print(MyClass.func1(10,20))
c = MyClass()
print(c.func1(50,12))
print(c.func2(15,6))
print(c.func3(23,5))
input()
