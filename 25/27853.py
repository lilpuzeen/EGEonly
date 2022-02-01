def div1(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for i in range(312614, 312651+1):
    if len(div1(i)) == 6:
        print(*div1(i))
