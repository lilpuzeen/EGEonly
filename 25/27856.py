def divodd(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(list(filter(lambda y: y % 2 != 0, d)))


for i in range(95632, 95650+1):
    if len(divodd(i)) == 6:
        print(*divodd(i))
