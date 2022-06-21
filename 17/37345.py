arr = [int(x) for x in open("37345.txt").readlines()]
# f = open("37345.txt")
# arr = []
# for line in f.readlines():
# 	arr.append(int(line))
count = 0
maxx = -100000000

for i in range(len(arr)):
	for j in range(i + 1, len(arr)):
		a = arr[i]
		b = arr[j]
		if (a * b) % 62 == 0:
			count += 1
			maxx = max(a + b, maxx)
print(count, maxx)