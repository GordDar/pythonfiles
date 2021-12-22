# -*- coding: utf-8 -*-
def gen(l):
    for e in l:
        yield from range(1, e+1)
l=[3,6]
for i in gen(l): print(i, end=" ")
input()
