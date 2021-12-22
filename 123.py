from random import randint
from collections import Counter
def counter(n):
    d=[randint(1, 10) for i in range(n)]
    t= list(Counter(d).most_common())
    d1=[]
    d2=[]
    for a, b in t:
        if d1==[]:
            d1.append(b)
            d2.append(a)
        elif d1!=[]:
            if b== d1[0] and a not in d2:
                d2.append(a)
            else:
                break
    d3 = sorted(d2)
    print(d1, d3, t)
    return f'Наибольшее число совпадений - {d1[0]}, наименьшее число из совпавших - {d3[0]}'


print(counter(10))


def switch_it_up(number):
    dict={0:'Zero', 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
    for key, value in dict.items():
        if key==number:
            return value


print(switch_it_up(9))


def dig_pow(n, p):
    d = []
    for i in str(n):
        d.append(i)
    sum=0
    for i in d:
        sum=sum+int(i)**p
        p+=1
    if sum%n==0:
        return int(sum/n)
    else:
        return -1


print(dig_pow(46288, 3))




