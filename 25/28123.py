def diveven(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(list(filter(lambda y: y % 2 == 0, d)))


for i in range(125256, 125330+1):
    if len(diveven(i)) == 6:
        print(*diveven(i))
