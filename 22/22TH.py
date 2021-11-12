def algo(x):
    a = 0
    b = 10
    while x > 0:
        d = x % 6
        if d > a: a = d
        if d < b: b = d
        x = x // 6
    return a+b  


for i in range(10000):
    if algo(i) == 7:
        print(i)
# 1) 177
# 2) 510
# 3) 26
# 4) 510
# 5) 17
