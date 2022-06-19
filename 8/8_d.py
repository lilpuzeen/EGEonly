from itertools import product

lets = list("АОУ")
count = 1
for item in product(lets, repeat=5):
	s = "".join(item)
	print(count, s)
	count += 1