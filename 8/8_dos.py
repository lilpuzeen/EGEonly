from itertools import product

lets = list("АБРТЫ")
count = 1
for item in product(lets, repeat=5):
	s = "".join(item)
	if s.count("Ы") == 0 and "АА" not in s:
		print(count, s)
	count += 1