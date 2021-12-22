# -*- coding: utf-8 -*-
def deco(f):
    print("Вызвана функция")
    return f
@deco
def func(x):
    return "x = {0}".format(x)
print(func(10))
input()
