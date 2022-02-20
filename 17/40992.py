f = open("40992.txt")
arr = [int(x) for x in f.readlines()]
oddsum = sum(list(filter(lambda x: x % 2 != 0, arr))) / len(list(filter(lambda x: x % 2 != 0, arr)))
maxx = -100000000
count = 0

for i in range(len(arr) - 1):
    a = arr[i]
    b = arr[i+1]
    if ((a % 5 == 0) or (b % 5 == 0)) and ((a < oddsum) or (b < oddsum)):
        count += 1
        if a+b > maxx:
            maxx = a+b

print(count, maxx)
