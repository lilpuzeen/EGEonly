def div(x):
    d = set()
    for y in range(2, int(x ** 0.5) + 1):
        if x % y == 0:
            d |= {y, x // y}
    return sorted(d)


for i in range(210235, 210300+1):
    if len(div(i)) == 4:
        print(*div(i))
