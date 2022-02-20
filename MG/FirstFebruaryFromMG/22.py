for i in range(1, 1000000):
    x = i
    L = 1
    M = 0
    while x > 0:
        M = M + 1
        if x % 2 != 0:
            L = L * (x % 8)
        x = x // 8
    if L == 21 and M == 3:
        print(i)
