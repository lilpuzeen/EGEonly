arr = []
for i in range(400, 500):
    d = [int(x) for x in list(set(str(i)))]
    arr.append(i/sum(d))

print(min(arr))
print([int(x) for x in sorted(set("423"))])