# def Solve1(n, k):
#     if n == k:
#         return 0
#     cubes = n//k
#     lines = cubes - 1
#     return (lines*cubes)*2

from math import ceil


def Solve2(x, y, n):
    if n < y:
        return ceil(n / x)
    answer = ceil((n / (x+y)) * 2)
    if (ceil((answer / 2) * (x + y)) != n) and (ceil((answer / 2) * (x + y) + y) >= n):
        return answer + 1
    else:
        return answer


if __name__ == '__main__':
    print(Solve2(int(input()), int(input()), int(input())))
