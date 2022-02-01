for i in range(1, 1000):
    x = i
    a = 0
    b = 10
    while x > 0:
        d = x % 6
        if d > a: a = d
        if d < b: b = d
        x = x // 6
    if a+b == 7:
        print(i)
