def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))


def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for i in range(105, 123):
    if p(i):
        print(i**4, div(i**4)[-1])
