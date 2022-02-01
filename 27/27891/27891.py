f = open("27891(B).txt")
arr = [int(x) for x in f.readlines()]

maxx = 10*10**-20
memory = 0

m7 = max(list(filter(lambda x: (x % 7 == 0) and (x % 2 != 0), arr)))
m2 = max(list(filter(lambda x: (x % 2 == 0) and (x % 7 != 0), arr)))
m14 = max(list(filter(lambda x: x % 14 == 0, arr)))
MAX = max(arr)

print(m7 * m2, m14 * MAX)
