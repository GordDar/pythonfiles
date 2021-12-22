# -*- coding: utf-8 -*-
try:
    try:
        x = 1/0
    except NameError:
        print("неопределенный идентификатор")
    except IndexError:
        print("несуществующий индекс")
    print("после встроенного обработчика")
except ZeroDivisionError:
    print("обработали исключение")
    x = "ничего"
print(x)
input()
