f = open("17(2).txt", "r+")
x = [int(y) for y in f.readlines()]

couples = []
count = 0
maxx = 10*10**-19

try:
    for i in range(len(x)):
        first = x[i]
        second = x[i + 1]
        if (first % 3 == 0) or (second % 3 == 0):
            count += 1
        if first + second > maxx:
            maxx = first + second
except IndexError:
    pass


print(count)
print(maxx)
