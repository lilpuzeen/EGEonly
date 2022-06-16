f = open("37360.txt")
arr = []
for line in f.readlines():
	arr.append(int(line))
count = 0
maxx = -10000000
for i in range(len(arr)):
	for j in range(i + 1, len(arr)):
		a = arr[i]
		b = arr[j]
		if (a + b) % 120 == 0:
			count += 1
			maxx = max(a+b, maxx)
print(count, maxx)
