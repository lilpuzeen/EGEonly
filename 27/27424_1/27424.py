f = open("27-B_demo.txt")
n = int(f.readline())
arr = []
for line in f.readlines():
    arr.append([int(x) for x in line.split()])
s = 0
for i in range(n):
    a = arr[i]
    s += max(a)
print(s, s%3)

deltas = set()
for j in range(n):
    b = arr[j]
    deltas.add(max(b) - min(b))
print(sorted(deltas)[:10])