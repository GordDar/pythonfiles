# -*- coding: utf-8 -*-
def gen2(n):
    for e in range(1, n+1):
        yield e*2
def gen(l):
    for e in l:
        yield from gen2(e)
l = [3,6]
for i in gen(l): print(i, end=" ")
input()    
