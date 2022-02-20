from math import factorial
m, n = map(int, input().split())


def combs(h, k):
    return (factorial(h)) / (factorial(k)*factorial(h-k))


C1 = combs(m, 3)
C2 = combs(n, 2) * m

print(int(C1+C2))
