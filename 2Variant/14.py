def calc(x, a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


g = 125 + 25**3 + 5**9
print(calc(g, 10, 5))
# 7 answer
