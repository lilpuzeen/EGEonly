f = open("26.txt")
n = int(f.readline())
a = [int(x) for x in f]
b = set(a)
ans = []

for i in range(n):
    for j in range(i+1, n):
        if (a[i] % 2 != 0) and (a[j] % 2 != 0):
            sr = (a[i] + a[j]) // 2
            if sr in b:
                ans.append(sr)

print(len(ans), max(ans))
