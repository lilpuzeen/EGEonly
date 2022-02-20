f = open("40733.txt")
arr = [int(x) for x in f.readlines()]
evensum = sum(list(filter(lambda x: x % 2 == 0, arr))) / len(list(filter(lambda x: x % 2 == 0, arr)))
maxx = -100000000
count = 0

for i in range(len(arr) - 1):
    a = arr[i]
    b = arr[i+1]
    if ((a % 3 == 0) or (b % 3 == 0)) and ((a < evensum) or (b < evensum)):
        count += 1
        if a+b > maxx:
            maxx = a+b

print(count, maxx)
