f = open('27-B_demo.txt')
n = int(f.readline())
s = [0]

for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    cmb = [a + b for a in s for b in pair]
    s = {x % 3: x for x in sorted(cmb)}  # Когда min список сортируем с помощью sorted(..., reverse(True)),values()

m = max(x for x in s if x % 3 != 0)  # Когда сумма min, то ищем минимальную ЛОГИЧНО!
print(m)
