def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


# lens = []
# for x in range(84052, 84130):
#     lens.append((x, len(div(x))))
# print(*sorted(lens, key=lambda x: x[1])[len(lens)-1])
#

for i in range(1000, 10000):
    if (i % 131 == 12) and (i % 132 == 98):
        print(i)
