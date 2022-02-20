for i in range(10000):
    s = i
    n = 5
    while s > 23:
        s = s - 5
        n = n * 2
    if n == 320:
        print(i)
