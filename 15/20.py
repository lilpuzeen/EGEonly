def dell(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(1, 1000):
        if not(((dell(x, 2)) <= (not(dell(x, 3)))) or (x + a >= 80)):
            break
    else:
        print(a)
    a += 1
