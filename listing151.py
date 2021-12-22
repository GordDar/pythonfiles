# -*- coding: utf-8 -*-
class MyClass():
    def __init__(self, s):
        self.s = s
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i> len(self.s) -1:
            raise StopIteration
        else:
            a = self.s[-self.i-1]
            self.i = self.i+1
            return a
s = MyClass("привет")
for a in s: print(a, end=", ")
input()
