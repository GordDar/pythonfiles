# -*- coding: utf-8 -*-
def func(x,y):
    for i in range(1, x+1):
        yield i**y
for n in func(10,2):
    print(n, end=" ")
print()
for n in func(10,3):
    print(n, end=" ")
input()

