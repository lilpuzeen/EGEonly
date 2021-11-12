def f(s):
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if n == 64:
        return s, n


for i in range(500):
    if f(i) is not None:
        print(i, f(i))