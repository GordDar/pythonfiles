# -*- coding: utf-8 -*-
try:
    x = 1/0
except (ZeroDivisionError, NameError):
    print("обработали исключение")
    x = "ничего"
print(x)
input()
