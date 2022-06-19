# P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
# ( (x ∈ A) → (x ∈ P) ) ∧ ( (x ∈ Q) → ¬(x ∈ A) )
# max
a = set(range(1000))


def f(x):
	P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
	Q = x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
	A = x in a
	return (A <= P) and (Q <= (not A))


for x in range(1000):
	if f(x) == 0:
		a.remove(x)
print(a)