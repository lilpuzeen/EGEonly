from itertools import product, permutations

arr = ['З', "А", "П", "И", "С", "Ь"]

b = list(permutations(arr))
filt = lambda x: (x[0] != "Ь") and ("АЬ" not in ''.join(x)) and ("ИЬ" not in ''.join(x))

print(len(list(filter(filt, b))))
