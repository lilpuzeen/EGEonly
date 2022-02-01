def f(n):
    if n > 2:
        return f(n-2) + f(n//2)
    else:
        return n


print(f(9))
