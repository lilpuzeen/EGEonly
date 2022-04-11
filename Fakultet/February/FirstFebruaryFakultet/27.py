f = open("27_B.txt")
n = int(f.readline())
s = [0]

for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    cmb = [a + b for a in s for b in pair]
    s = {x % 109: x for x in sorted(cmb)}.values()

m = max(x for x in s if x % 109 != 0)
print(m)
