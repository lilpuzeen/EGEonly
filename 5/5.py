n = int(input())
r = bin(n)[2:]

digits = [int(x) for x in tuple(r)]
r += str(sum(digits) % 2)
digits = [int(x) for x in tuple(r)]
r += str(sum(digits) % 2)

print(int(r, 2))
