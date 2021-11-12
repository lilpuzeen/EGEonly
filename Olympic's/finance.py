from itertools import product, permutations
n = int(input())
k = int(input())
arr = [x for x in range(n, k+1)]
arr1 = []
print(list(product(arr)))
