def calc(x, a, b):
    s = ""
    x = int(str(x), a)
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


a = 7**1003 + 6*7**1104 - 3*7**57 +294
x = calc(a, 10, 7)
arr = [int(i) for i in list(x)]
print(sum(arr))
