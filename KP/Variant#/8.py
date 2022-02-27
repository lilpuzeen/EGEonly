from itertools import product

letters = ["С", "О", "Л", "Н", "Ц", "Е"]
arr = list(product(letters, repeat=6))
arr = list(filter(lambda x: x.count("О") <= 2 and x.count("Ц") == 1, arr))
print(len(arr))

