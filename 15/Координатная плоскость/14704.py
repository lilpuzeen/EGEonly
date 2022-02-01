a = 1
while True:
    for x in range(1000):
        for y in range(1000):
            if not(((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6))):
                break
        else:
            continue
        break
    else:
        print(a)
    a += 1

#  ответ max - min + 1
