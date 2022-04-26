from itertools import product

lets = ["А", "В", "Д", "П", "Р"]


count = 1
for item in product(lets, repeat=4):
	s = "".join(item)
	if s.count("А") == 0 and all(s.count(x) <= 1 for x in lets):
		print(count, s)
	count += 1
