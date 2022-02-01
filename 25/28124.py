def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


lens = []
for i in range(568023, 569230+1):
    lens.append((i, len(div(i))))

print(sorted(lens, key=lambda x: x[1]))
