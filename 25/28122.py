def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for i in range(489421, 489440+1):
    if len(div(i)) == 4:
        print(*div(i))
