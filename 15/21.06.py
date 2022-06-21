# def dell(n, m):
#     return n % m == 0
#
#
# a = 1
# while True:
#     for x in range(1, 1000):
#         if not(dell(x, a) or ((60 <= x <= 80) <= (not(dell(x, 22))))):
#             break
#     else:
#         print(a)
#     a += 1


from itertools import combinations


def f(x):
    B = 10 <= x <= 24
    C = 70 <= x <= 89
    A = a1 <= x <= a2
    return A or B or (not C)


Ox = [i/4 for i in range(9*4, 91*4)]
m = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2 - a1)
print(min(m))
