# 46
for i in range(10000):
	n = bin(i)[2:]

	arr = sum([int(x) for x in list(n)])
	n += str(arr % 2)

	arr = sum([int(x) for x in list(n)])
	n += str(arr % 2)

	if int(n, 2) > 43:
		print(int(n, 2))
