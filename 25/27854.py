def diveven(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(list(filter(lambda y: y % 2 == 0, d)))


for i in range(110203, 110245):
    if len(diveven(i)) == 4:
        print(*diveven(i))
