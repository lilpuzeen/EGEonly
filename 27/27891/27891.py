f = open("27891(A).txt")
n = int(f.readline())
arr = [int(x) for x in f.readlines()]
k = 14
maxx = float("-inf")
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        a = arr[i]
        b = arr[j]
        if (a*b) % k == 0:
            maxx = max(a*b, maxx)
print(maxx)