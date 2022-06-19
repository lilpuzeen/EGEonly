# p 15 33
# q 35 48
# max
from itertools import combinations
def f(x):
	P = 15 <= x <= 33
	Q = 35 <= x <= 48
	A = a1 <= x <= a2
	return (A and (not Q)) <= (P or Q)


Ox = [i/4 for i in range(14*4, 50*4)]
m = []

for a1, a2 in combinations(Ox, 2):
	if all(f(x) == 1 for x in Ox):
		m.append(a2 - a1)
print(max(m))