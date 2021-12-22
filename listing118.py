# -*- coding: utf-8 -*-
arr = ["единица1", "Единый", "Единица2"]
arr.sort(key=lambda x: x.lower())
for i in arr:
    print(i, end=" ")
input()
