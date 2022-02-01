A = [x for x in range(100)]
while True:
    for x in range(100):
        if not(((x in A) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in A))):
            A.remove(x)
            break
    else:
        print(x, A)
        continue
# Grob
