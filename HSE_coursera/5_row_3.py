n = int(input())

if n == 1:
    for i in range(10, 1 - 1, -1):
        if i % 2 != 0:
            print(i, end=" ")
    exit(0)

for i in range(10**(n), 10**(n - 1) - 1, -1):
    if i % 2 != 0:
        print(i, end=" ")
