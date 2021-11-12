from typing import List


def isPrime(arr: List):
    empty = []
    for item in arr:
        k = 0
        for j in range(1, item+1):
            if item % j == 0:
                k += 1
        if k == 2:
            empty.append((arr.index(item) + 1, item))
    return empty


if __name__ == '__main__':
    x = [int(x) for x in range(245690, 245756 + 1)]
    print(isPrime(x))
