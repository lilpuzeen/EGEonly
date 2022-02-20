f = open("27-B_demo.txt", "r+")
arr = []
for line in f.readlines():
    myline = line.split()
    arr.append((int(myline[0]), int(myline[1])))

s = 0
minn = 20001
n = len(arr)

for i in range(n):
    s += max(arr[i])
    d = abs(arr[i][0] - arr[i][1])
    if d % 3 != 0:
        minn = min(d, minn)

if s % 3 != 0:
    print(s)
else:
    print(s - minn)
