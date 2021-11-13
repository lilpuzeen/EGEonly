from collections import Counter
file = open("kp.txt")
strings = [str(x) for x in file.readlines()]
strokes = []
for i in range(len(strings)):
    strokes.append((i, strings[i].count("A")))
minn = 10*10**8
for line in strokes:
    if line[1] < minn:
        minn = line[1]
        ind = line[0]

r = strings[548]
Vs = []
for i in range(len(strings)):
    Vs.append(strings[i].count("V"))

print(sum(Vs))
