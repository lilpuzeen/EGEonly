f = open("40999.txt")
string = f.readline()
maxx = -100000000
count = 1
countA = 1

for i in range(len(string)):
    if string[i] == "E":
        count = 0
        countA = 0
        continue
    elif string[i] == "A":
        countA += 1
    count += 1
    if (count > maxx) and (countA >= 3):
        maxx = count

print(maxx)
