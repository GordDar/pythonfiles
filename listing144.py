# -*- coding: utf-8 -*-
try:
    x = 1/0
except (ZeroDivisionError, NameError) as err:
    print(err.__class__.__name__)
    print(err)
input()
