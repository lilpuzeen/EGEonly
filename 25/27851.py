for i in range(210235, 210300 + 1):
    k = 0
    del1 = 0
    del2 = 0
    del3 = 0
    del4 = 0
    for x in range(2, i):
        if i % x == 0:
            k += 1
            if k == 1:
                del1 = x
            if k == 2:
                del2 = x
            if k == 3:
                del3 = x
            if k == 4:
                del4 = x
    if k == 4:
        print(f"Делители числа {i}: {del1}, {del2}, {del3}, {del4}")
