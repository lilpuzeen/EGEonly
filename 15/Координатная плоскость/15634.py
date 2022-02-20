a = 1
while True:
    for x in range(1000):
        for y in range(1000):
            if not((y + 2*x < a) or (x > 30) or (y > 20)):
                break
        else:
            continue
        break
    else:
        print(a)
    a += 1
