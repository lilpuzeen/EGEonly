# P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
# ((x ∈ P) → (x ∈ A)) ∨ (¬(x ∈ A) → ¬(x ∈ Q))
# min
a = set()


def f(x):
	P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
	Q = x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
	A = x in a
	return (P <= A) or ((not A) <= (not Q))


for x in range(1000):
	if f(x) == 0:
		a.add(x)
print(a)