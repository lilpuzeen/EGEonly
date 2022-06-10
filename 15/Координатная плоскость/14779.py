#  если вопрос "сколько целых значений" то ответ: max - min + 1
a = 1
while True:
    for x in range(1000):
        for y in range(1000):
            if not(((x < 5) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 5))):
                break
        else:
            continue
        break
    else:
        print(a)
    a += 1
filter()