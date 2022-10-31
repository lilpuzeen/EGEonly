# def maximum(a: int, b: int) -> int:
#     return (abs(a - b) + a + b) // 2


from math import factorial


def combinations(n: int, k: int) -> float:
    return factorial(n) / (factorial(k) * factorial(n - k))


for i in range(1, 20):
    for j in range(i+1, 20):
        if combinations(j, i) == 210:
            print(i, j)
