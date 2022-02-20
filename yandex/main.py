import math


def fnc1(a, x):
    return round(a * (x ** (a - 1)), 3)


def fnc2(a, x):
    return round(math.log1p(a) * (a ** x), 3)


def ln(x):
    if x > 0:
        return round(1 / x, 3)
    return None


def tg(x):
    return round(1 / (math.cos(x) ** 2), 3)


def ctg(x):
    return round(-1 / (math.sin(x) ** 2), 3)


string = input()
n = float(input())
if string == 'ln(x)':
    print(ln(n))
elif string == 'tg(x)':
    print(tg(n))
elif string == 'ctg(x)':
    print(ctg(n))
elif string[0:2] == 'x^':
    print(fnc1(int(string[-1]), n))
else:
    print(fnc2(int(string[0]), n))
