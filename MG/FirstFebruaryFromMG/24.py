from re import findall
from collections import Counter
f = open("24-164.txt")
arr = [str(x) for x in f.readlines()]
maxx = -100000
countK = 0

for s in arr:
    c, letter = max(findall("(.)(\\1*)", s), key=lambda x: len(x[1]))
    if len(letter) + 1 > maxx:
        maxx = len(letter) + 1
        c1 = c
        ind = arr.index(s)

print(ind, c1, maxx)
print(Counter(arr[161]).most_common(1))

for item in arr:
    countK += item.count("K")

print(countK)
