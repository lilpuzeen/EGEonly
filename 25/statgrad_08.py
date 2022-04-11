def p(x):
	return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def div(x):
	d = set()
	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			d |= {i, x//i}
	return sorted(d)


for i in range(300_000_001, 300_001_001):
	if p(i):
		continue
	arr = div(i)
	if len(arr) > 5:
		M = arr[4]
		print(M)


