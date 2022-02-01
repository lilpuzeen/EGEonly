def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for i in range(200_000_000+1, 200_010_000+1):  # обратить внимание на условие задачи!!! большее 200_000_000!!!! =>
    # => range(200_000_000+1)
    if p(i):
        continue
    if len(div(i)) >= 5:
        M = div(i)[0]*div(i)[1]*div(i)[2]*div(i)[3]*div(i)[4]
        if (M > 0) and (M < i):
            print(i, M)
