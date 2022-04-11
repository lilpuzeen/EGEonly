from itertools import product

lets = ["А", "Б", "Р", "Т", "Ы"]

count = 1
for item in product(lets, repeat=5):
	s = "".join(item)
	if "АА" not in s and "ЫЫ" not in s:
		print(count, s)
		break
	else:
		count += 1