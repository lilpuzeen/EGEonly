def p(x):
	return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def div(x):
	d = set()
	for i in range(1, int(x**0.5)+1):
		if x % i == 0:
			d |={i, x // i}
	return sorted(d)


for i in range(201455, 201470+1):
	arr = div(i)
	if len(arr) == 4:
		print(*arr)
s = "101101"
s = s.removeprefix()