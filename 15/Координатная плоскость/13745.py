a = 1
while True:
    for x in range(1000):
        for y in range(1000):
            if not(((x <= 9) <= (x*x <= a)) and ((y*y <= a) <= (y <= 9))):
                break
        else:
            continue
        break
    else:
        print(a)
    a += 1
