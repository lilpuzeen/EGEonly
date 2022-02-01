def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for y in range(101_000_000, 102_000_000 + 1):
    t = int((y // 2) ** 0.5)
    if 2*t**2 == y and p(t):
        print(y)
