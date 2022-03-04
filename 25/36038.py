def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))  # определение простых чисел


def div(x):  # поиск делителей числа
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x // i}  # запись пар делителей
    return sorted(d)


for i in range(452022, 453000):  # решение
    if p(i):
        continue
    arr = div(i)
    M = arr[0] + arr[-1]
    if M % 7 == 3:
        print(i, M)
