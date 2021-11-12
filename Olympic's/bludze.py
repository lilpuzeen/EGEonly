def blude(n, k):
    if n == k:
        return 0
    return 2*n*(n//k-1)


if __name__ == '__main__':
    print(blude(int(input()), int(input())))
