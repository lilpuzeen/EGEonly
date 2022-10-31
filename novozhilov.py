# 8
from itertools import permutations

words = list(permutations("КЛАБХАУС"))
count = 0
bad = False

for word in words:
	for i in range(len(word) - 1):
		let1 = word[i]
		let2 = word[i + 1]
		if let1 == let2:
			bad = True
			break
	else:
		if bad:
			count += 1
			bad = False

print(count)