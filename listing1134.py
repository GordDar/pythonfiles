# -*- coding: utf-8 -*-
def f():
    local1 = 54
    glob2 = 25
    print("Глобальные внутри", sorted(globals().keys()))
glob1 = 10
glob2 = 88
f()
print("глобальные вне", sorted(globals().keys()))
input()
