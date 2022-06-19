from itertools import combinations


def f(x):
	P = 130 <= x <= 171
	Q = 150 <= x <= 185
	A = a1 <= x <= a2
	return P <= ((Q and (not A)) <= (not P))


Ox = [i/4 for i in range(128*4, 187*4)]
m = []

for a1, a2 in combinations(Ox, 2):
	if all(f(x) == 1 for x in Ox):
		m.append(a2 - a1)

print(min(m))
