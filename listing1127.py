# -*- coding: utf-8 -*-
def f(n):
    if n ==0 or n ==1: return 1
    else:
        return n*f(n-1)
while True:
    x = input("Введите число: ")
    if x.isdigit():
        x = int(x)
        break
    else:
        print("это не число")
print("Факториал {0} = {1}".format(x, f(x)))
input()
