# -*- coding: utf-8 -*-
print("Введите слово !stop! для получения результата")
summa = 0
while True:
    x = input("Введите число: ")
    if x=="stop":
        break
    try:
        x = int(x)
    except ValueError:
        print("необходимо ввести число!")
    else:
        summa +=x
print("Сумма чисел равна: ", summa)
input()
