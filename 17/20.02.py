arr = [int(x) for x in open("17_20.txt").readlines()]
maxx = float("-inf")
count = 0
mn = min(arr)
for i in range(len(arr) - 1):
	a = arr[i]
	b = arr[i + 1]
	if (a % 117 == mn) or (b % 117 == mn):
		count += 1
		maxx = max(maxx, a + b)
print(count, maxx)
