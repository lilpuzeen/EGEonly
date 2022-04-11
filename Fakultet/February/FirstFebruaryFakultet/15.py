a = 1
while True:
    for x in range(1000):
        for y in range(1000):
            if not((2*x + 3*y < 30) or (x + y >= a)):
                break
        else:
            continue
        break
    else:
        print(a)
    a += 1
