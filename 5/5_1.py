for i in range(100, 1000):
	a, b, c = i // 100, i // 10 % 10, i % 10
	u, v = a + b, b + c
	if u > v:
		s = str(v) + str(u)
		if s == "1412":
			print(i)
			break
	else:
		s = str(u) + str(v)
		if s == "1412":
			print(i)
			break