n = bin(91)[2:]
n = "0" + n

n = n[1:] + "0"
n = n[1:] + "0"

n = int(n, 2)
n -= 1


n = bin(n)[2:]
n = "0" + n

n = n[1:] + "0"
n = n[1:] + "0"

n = int(n, 2)
n -= 1
print(n)
