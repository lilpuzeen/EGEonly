arr = [int(x) for x in input().split()]


if len(arr) % 2 == 0:
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
else:
    last = arr[-1]
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    arr[-1] = last

print(*arr)
