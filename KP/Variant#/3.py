# ДЕЛ(A, 7) ∧ (ДЕЛ(240, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(780, x)))
def dell(n, m):
    return n % m == 0


A = 1
while True:
    for x in range(1, 100000):
        if not (dell(A, 7) and (dell(240, x) <= ((not dell(A,x)) <= (not dell(780, x))))):
            break
    else:
        print(A)
    A += 1