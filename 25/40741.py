def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for i in range(10_000_000+1, 10_010_000):
    if p(i):
        continue
    M = div(i)[-1] + div(i)[-2]
    if M < 10000:
        print(i, M)
