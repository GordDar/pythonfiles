# -*- coding: utf-8 -*-
passw = input("Введите пароль: ")
def test_passw(p):
    if p == "10":
        return p
    else:
        return lambda: "ДОступ закрыт"
    return test_passw
@test_passw(passw)
def func():
    return "Доступ открыт"
print(func())
input()
