m, n = map(int, input().split())

a = (m / 6) * (((3 * n) * (n - 1)) + ((m - 1) * (m - 2)))
print(int(a))
