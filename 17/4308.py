arr = [int(x) for x in open("4308.txt").readlines()]
count = 0
maxx = float("-inf")

for i in range(len(arr) - 3):
    a, b, c, d = arr[i], arr[i + 1], arr[i + 2], arr[i + 3]
    if (a % 2 != b % 2) and (b % 2 != c % 2) and (c % 2 != d % 2):
        count += 1
        maxx = max(maxx, a+b+c+d)
print(count, maxx)