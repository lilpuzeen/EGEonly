f = open("39764.txt")
arr = [int(x) for x in f.readlines()]
count = 0
maxx = 0

for i in range(1, len(arr) - 1):
    a = arr[i-1]
    b = arr[i]
    c = arr[i+1]
    s = sorted([a, b, c])
    if s[2]**2 == s[0]**2 + s[1]**2:
        count += 1
        if sum(s) > maxx:
            maxx = sum(s)
print(count, maxx)
# я в ахуе в ответах к задачам могут быть и 0 0 это пиздец ахуеть