def calc(x, a, b):
    x = int(str(x), a)
    s = ""
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


a = 4**103 + 3*4**444 - 2*4**44 + 67
b = calc(a, 10, 4)
# print(b.count("3"))
print(calc(200, 3, 10))
