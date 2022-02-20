def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

#
# for x in range(123456789, 223456789+1):
#     t = x
#     while True:
#         if int(t**0.25)**4 == t and p(int(t**0.25)):
#             print(x, div(t)[len(div(t))-1])
#             break
#         else:
#             break

print(p(131))