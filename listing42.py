# -*- coding: utf-8 -*-
print("Какой операционной системой вы пользуетесь?")
os = input("Введите число: ")
if os =="1":
    print("вы выбрали windows 10")
elif os == "2":
    print("вы выбрали windows 8.1")
elif not os:
    print("Вы не ввели число")
else:
    print("мы не смогли определить вашу os")
input()
