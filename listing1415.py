# -*- coding: utf-8 -*-
try:
    x = -3
    assert x>=0, "Сообщение об ошибке"
except AssertionError as err:
    print(err)    
input()
