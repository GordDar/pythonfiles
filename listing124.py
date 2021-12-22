# -*- coding: utf-8 -*-
import math
def hasattr_math(attr):
    if hasattr(math, attr):
        return "атрибут существует"
    else:
        return "Атрибут не существует"
print(hasattr_math("pi"))
print(hasattr_math("x"))
input()
