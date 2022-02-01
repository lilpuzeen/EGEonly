a = 1
while True:
    for x in range(1000):
        for y in range(1000):
            if not(((x < a) <= (x**2 < 100)) and ((y**2 <= 64) <= (y <= a))):
                break
        else:
            continue
        break
    else:
        print(a)
    a += 1
