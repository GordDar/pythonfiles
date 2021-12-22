d = {"x":1, "y":2, "z":3}
import copy
d1 = copy.deepcopy(d)
print(d1)
key = ("a", "b")
value = (1,2)
print({k:v for (k,v) in zip(key, value)})
input()
