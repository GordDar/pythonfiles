# -*- coding: utf-8 -*-
class MyClass:
    def func(self, x):
        raise NotIMplementedError("Необходимо переопределить метод")
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
except NotImplementedError as msg:
    print(msg)
input()
