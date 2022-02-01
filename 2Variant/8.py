from itertools import permutations, product

arr = ['-', '.']
print(list(permutations(arr, r=5)))
print(len(list(product(arr, repeat=5)))+len(list(product(arr, repeat=4)))+len(list(product(arr, repeat=3)))+len(list(product(arr, repeat=2)))+len(list(product(arr, repeat=1))))
