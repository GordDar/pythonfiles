# -*- coding: utf-8 -*-
class Class1:
    def func1(self):
        print("Метод func1 клаcса Class1")
    def func2(self):
        print("Метод func2 клаcса Class1")
class Class2(Class1):
    def func3(self):
        print("Метод func3 класса Class2")
c = Class2()
c.func1()
c.func2()
c.func3()
input()
