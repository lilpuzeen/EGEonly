# 12345?7?8
for i in "0123456789":
	for j in "0123456789":
		s = "12345" + i + "7" + j + "8"
		n = int(s)
		if n % 23 == 0:
			print(n, n // 23)