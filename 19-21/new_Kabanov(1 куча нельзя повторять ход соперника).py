def f(s, p, c, m):
	if s >= 43:
		return c%2==m%2
	if c == m:
		return 0

	h = []
	if p != "+1":
		h += [f(s+1, "+1", c+1, m)]
	if p != "+2":
		h += [f(s+2, "+2", c+1, m)]
	if p != "*2":
		h += [f(s*2, "*2", c+1, m)]

	return any(h) if (c+1)%2==m%2 else all(h)


for s in range(1, 43):
	for m in range(1, 5):
		if f(s, "", 0, m):
			print(s, m)
			break
