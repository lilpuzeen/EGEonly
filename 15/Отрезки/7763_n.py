# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
from itertools import combinations
def f(x):
	P = 5 <= x <= 30
	Q = 14 <= x <= 23
	A = a1 <= x <= a2
	return (P == Q) <= (not A)


Ox = [i/4 for i in range(4*4, 32*4)]
m = []

for a1, a2 in combinations(Ox, 2):
	if all(f(x) == 1 for x in Ox):
		m.append(a2 - a1)
print(round(max(m)))
