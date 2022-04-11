# 27686
s = open("27686.txt").readline()
s = s.replace("Y", " ").replace("Z", " ").split(" ")
print("Ответ на первое задание:", max(map(len, s)))
# Ответ 19

# 38602
s = open("38602.txt").readline()
count = 0
maxx = -10000000
for i in range(1, len(s)):
    prev = s[i-1]
    curr = s[i]
    if (prev == "P") and (curr == "P"):
        count = 0
    count += 1
    if count > maxx:
        maxx = count

print("Ответ на второе задание:", maxx)
# Ответ 188
