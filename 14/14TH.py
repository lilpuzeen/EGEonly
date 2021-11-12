a = 49**10 + 7**30 - 49
i = 0

while a > 0:
    n = a % 7
    if n == 6:
        i += 1
    a //= 7
print(i)
