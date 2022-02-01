f = open("17.txt", "r+")
arr = [int(x) for x in f.readlines()]
maxx = -1000000
count = 0
for i in range(len(arr) - 1):
    a = arr[i]
    b = arr[i+1]
    if ((a*b) % 15 == 0) and ((a + b) % 7 == 0):
        count += 1
        if (a+b) > maxx:
            maxx = a+b
print(count, maxx)
