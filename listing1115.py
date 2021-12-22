# -*- coding: utf-8 -*-
def func(*t, **d):
    for i in t:
        print(i, end=" ")
    for i in d:
        print("{0}: {1}".format(i, d[i], end=" "))
func(1,2,3, a=4, b=5)
input()
