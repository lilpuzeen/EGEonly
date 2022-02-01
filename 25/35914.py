def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


for y in range(45_000_000, 50_000_000 + 1):
    t = y
    while t % 2 == 0:
        t = t // 2
    if int(t ** 0.25) ** 4 == t and p(int(t ** 0.25)):
        print(y)
