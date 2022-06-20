f = open("27B.txt")
n = int(f.readline())

arr = []
for i in range(n):
    s, k = map(int, f.readline().split())
    c = k // 36 if k % 36 == 0 else (k // 36) + 1
    arr.append([s, c])
print(arr)
