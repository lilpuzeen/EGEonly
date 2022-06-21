arr = [int(x) for x in open("45251.txt").readlines()]

count = 0
maxx = -10000000
min21 = 1000000000

for item in arr:
	if item % 21 == 0:
		min21 = min(item, min21)

for i in range(len(arr) - 1):
	a = arr[i]
	b = arr[i + 1]
	if (a % min21 == 0) or (b % min21 == 0):
		count += 1
		maxx = max(a + b, maxx)
print(count, maxx)