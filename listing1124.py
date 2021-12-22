# -*- coding: utf-8 -*-
def deco(f):
    print("Вызвана функция")
    return f

def func(x):
    return "x = {0}".format(x)
print(deco(func(10)))
input()
