# -*- coding: utf-8 -*-
n = input("Введите 1 для вызова первой функции: ")
if n ==1:
    def f():
        print("ввели число 1")
else:
    def f():
        print("ввели другое число")
f()
input()
