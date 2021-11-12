n = int(input())
d = int(input())
arr = [int(input()) for i in range(n)]
x = 0
while True:
    maxx = 0
    indx = 0
    lians = arr[x] // d
    for k in range(1, lians + 1):
        if arr[x + k] >= maxx:
            maxx = arr[x + k]
            indx = x + k
        if x + k == n - 1:
            break
    x = indx
    if (arr[x] < d) or (x == n-1):
        print(x + 1)
        break
