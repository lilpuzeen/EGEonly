f = open("17-1.txt")
arr = [int(x) for x in f.readlines()]
count = 0
minn = 10000000000

for i in range(len(arr) - 1):
    a = arr[i]
    b = arr[i+1]
    if ((a % 7 == 0) and (b % 17 != 0)) or ((b % 7 == 0) and (a % 17 != 0)):
        count += 1
        if a+b < minn:
            minn = a+b

print(count, minn)
