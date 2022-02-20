for i in range(1000):
    n = i
    n = bin(n)[2:]
    arr = [int(x) for x in tuple(n)]
    if sum(arr) % 2 != 0:
        n += "11"
    elif sum(arr) % 2 == 0:
        n += "00"
    if int(n, 2) > 114:
        print(int(n, 2))
