def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for i in range(600000, 600100):
    ends = [x % 10 for x in div(i)]
    if ends.count(7) >= 1:
        print(i, div(i))
