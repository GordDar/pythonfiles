# -*- coding: utf-8 -*-
class MyError(Exception):
    def __init__(self, value):
        self.msg = value
    def __str__(self):
        return self.msg
try:
    raise MyError("описание исключения")
except MyError as err:
    print(err)
    print(err.msg)
raise MyError("описание исключения")
input()
