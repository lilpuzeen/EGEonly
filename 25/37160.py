def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for i in range(500000, 500100):
    ends = [x % 10 for x in div(i)]
    if ends.count(8) >= 1:
        print(i, div(i))
