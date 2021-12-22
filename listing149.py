# -*- coding: utf-8 -*-
class MyClass:
    def __enter__(self):
        print("Вызван метод __enter__()")
        return self
    def __exit__(self, Type, Value, Trace):
        print("Вызван метод __exit__()")
        if Type is None:
            print("Исключений не возникло")
        else:
            print("VAlue: ", Value)
            return False
print("Последовательность при отсутствии исключения: ")
with MyClass():
    print("Блок внутри with")
print("\nПоследовательность при наличии исключения:")
with MyClass() as obj:
    print("БЛок внутри with")
    raise TypeError("Исключение TypeError")
input()
