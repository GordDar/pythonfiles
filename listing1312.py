# -*- coding: utf-8 -*-
class Mixin:
    attr = 0
    def mixin_method(self):
        print("Метод примеси")
class Class1(Mixin):
    def method1(self):
        print("метод класса Class1")
class Class2(Class1, Mixin):
    def method2(self):
        print("метод класса Class2")
c1 = Class1()
c1.method1()
c1.mixin_method()
c2 = Class2()
c2.method1()
c2.method2()
c2.mixin_method()
input()
