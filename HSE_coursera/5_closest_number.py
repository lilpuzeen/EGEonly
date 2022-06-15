n = int(input())
arr = [int(x) for x in input().split()]
x = int(input())

minn = 1000000000000000
for i in range(n):
    delta = abs(arr[i] - x)
    if delta < minn:
        digit = arr[i]
        minn = delta

print(digit)
