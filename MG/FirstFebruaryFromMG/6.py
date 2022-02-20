for i in range(1, 10000):
    s = i
    n = 1
    while s <= 45:
        s = s + 4
        n = n * 2
    if n == 256:
        print(i)
