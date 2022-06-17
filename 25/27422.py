for x in range(174457, 174505 + 1):
    k = 0
    del1 = 0
    del2 = 0
    for i in range(2, x):  ## генератор возможных делителей числа х
        if x % i == 0:  ## проверка явл. ли x дел х
            k = k + 1
            if k == 1:
                del1 = i
            if k == 2:
                del2 = i
    ########## поиск делителей для числа х завершен
    if k == 2:
        print(x,del1, del2)

print()
print()


def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for i in range(174457, 174505+1):
    if p(i):
        continue
    arr = div(i)
    if len(arr) == 2:
        print(i, *arr)