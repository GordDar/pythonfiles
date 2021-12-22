# -*- coding: utf-8 -*-
class Version:
    def __init__(self, major, minor, sub):
        self.__major = major
        self.__minor = minor
        self.__sub = sub
    def __str__(self):
        return f'{self.__major}.{self.__minor}.{self.__sub}'
    def __getitem__(self, k):
        if k == "major":
            return self.__major
        if k == "minor":
            return self.__minor
        if k == "sub":
            return self.__sub
        else:
            raise IndexError
    def __setitem__(self, k, v):
        if k == "major":
            self.__major = v
        if k == "minor":
            self.__minor = v
        if k == "sub":
            self.__sub = v
        else:
            raise IndexError
    def __delitem__(self, k):
        raise TypeError
    def __contains__(self, v):
        return v =="major" or v =="minor" or v =="sub"
v = Version(3,6,4)
print(v["major"])
v["sub"] = 5
print(str(v))
input()
