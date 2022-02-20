def p(x):
    return x > 1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))


def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return list(filter(p, sorted(d)))


for i in range(450_001, 1_000_000+1):
    if p(i):
        continue
    M = div(i)[len(div(i)) - 1] - div(i)[0]
    if M % 29 == 11:
        print(i, M)
