# -*- coding: utf-8 -*-
from enum import Enum
class VE(Enum):
    V2_7 = "2.7"
    V3_6 = "3.6"
    def describe(self):
        return self.name, self.value
    def __str__(self):
        return f'{__class__.__name__}.{self.name}:{self.value}'
    @classmethod
    def getmostfresh(cls):
        return cls.V3_6
d = VE.V2_7.describe()
print(VE.getmostfresh())
input()
