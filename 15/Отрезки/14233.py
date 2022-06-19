# P = [17, 46] и Q = [22, 57]
# ¬(x ∈ A) →(((x ∈ P) ⋀ (x ∈ Q)) → (x ∈ A))
# min
from itertools import combinations


def f(x):
	P = 17 <= x <= 46
	Q = 22 <= x <= 57
	A = a1 <= x <= a2
	return (not A) <= ((P and Q) <= A)


Ox = [i/4 for i in range(15*4, 60*4)]
m = []
for a1, a2 in combinations(Ox, 2):
	if all(f(x) == 1 for x in Ox):
		m.append(a2 - a1)
print(min(m))