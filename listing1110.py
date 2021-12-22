# -*- coding: utf-8 -*-
def summa(a,b,c):
    return a+b+c
d = {"a": 1, "b": 5, "c": 2}
print(summa(**d))
t,d1 = (1,2), {"c":5}
print(summa(*t, **d1))
input()
