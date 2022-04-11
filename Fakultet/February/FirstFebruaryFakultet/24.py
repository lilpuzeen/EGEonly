s = open("24.txt").readline()
count = 0
maxx = -100000


for i in range(len(s) - 3):
    l1 = s[i]
    l2 = s[i+1]
    l3 = s[i+2]
    l4 = s[i+3]
    if l1 == "X" and l2 == "Z" and l3 == "Z" and l4 == "Y":
        count = 0
        count += 3
    else:
        count += 1
    if count > maxx:
        maxx = count

print(maxx)
