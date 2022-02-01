for i in range(1000, 10000):
    arr = tuple(str(i))
    arr = [int(x) for x in arr]
    a = arr[0]+arr[1]
    b = arr[1]+arr[2]
    c = arr[2]+arr[3]
    newarr = [a, b, c]
    newarr = sorted(newarr)
    newarr.pop(0)
    newarr = [str(x) for x in newarr]
    if "".join(newarr) == "1315":
        print(i)
