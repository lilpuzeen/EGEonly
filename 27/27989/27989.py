f = open("27989_B.txt")
n = int(f.readline())

arr = [int(x) for x in f.readlines()]

count = 0
maxx = max(arr)
m26 = [x for x in arr if x % 26 == 0]
m2 = [x for x in arr if (x % 2 == 0) and (x % 26 != 0)]
m13 = [x for x in arr if x % 13 == 0 and (x % 26 != 0)]

print(len(m2) * len(m13) + len(m26) * (len(arr) - len(m26)))