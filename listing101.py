# -*- coding: utf-8 -*-
import time
d = ["пон", "втр", "срд", "чтв", "птн", "суб", "вос"]
m = ["", "j", "f", "m", "a", "m", "j", "j", "a", "s", "o", "n", "d"]
t = time.localtime()
print("Сегодня:\n%s %s %s %s %02d:%02d:%02d\n%02d.%02d.%02d" % (d[t[6]], t[2], m[t[1]], t[0], t[3], t[4], t[5], t[2], t[1], t[0]))
input()
