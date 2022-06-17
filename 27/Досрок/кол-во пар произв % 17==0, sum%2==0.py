f = open("27B.txt")
n = int(f.readline())
k170 = k171 = k0 = k1 = 0

for i in range(n):
	x = int(f.readline())
	if x % 17 == 0 and x % 2 == 0: k170 += 1
	if x % 17 == 0 and x % 2 != 0: k171 += 1
	if x % 17 != 0 and x % 2 == 0: k0 += 1
	if x % 17 != 0 and x % 2 != 0: k1 += 1

print(k170 * (k170 - 1) // 2 + k171 * (k171 - 1) // 2 + k170 * k0 + k171 * k1)
