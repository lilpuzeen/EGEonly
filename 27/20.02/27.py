f = open("27A.txt")
n = int(f.readline())

arr = []
for i in range(n):
    s, k = map(int, f.readline().split())
    c = k // 36 if k % 36 == 0 else (k // 36) + 1
    arr.append([s, c])

mn = float("inf")
for i in range(n):
    s = 0
    for j in range(n):
        s += abs(arr[i][0] - arr[j][0]) * arr[j][1]
    mn = min(mn, s)
print(mn)