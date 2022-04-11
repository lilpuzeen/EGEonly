def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for i in range(174457, 174505+1):
    if len(div(i)) == 2:
        print(*div(i))
