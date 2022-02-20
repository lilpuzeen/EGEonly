def f(x, a):
    return ((x in a) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in a))


a = set([i / 10 for i in range(-10000 * 10, 10000 * 10)])

for x in [i / 10 for i in range(-10000 * 10, 10000 * 10)]:
    if not f(x, a):
        a.remove(x)

print(sorted(a))
