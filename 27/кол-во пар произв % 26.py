f = open("27A.txt")
n = int(f.readline())
k26 = k13 = k2 = k = 0

for i in range(n):
	x = int(f.readline())
	if x % 26 == 0:
		k26 += 1
	elif x % 13 == 0:
		k13 += 1
	elif x % 2 == 0:
		k2 += 1
	else:
		k += 1
print(k26*(k26-1)//2 + k26*(k13+k2+k) + k2*k13)
