s = open("24 (1).txt").readline()
s = s.replace("B", "X").replace("C", "X").replace("D", "X").replace("O", "A")
count = 0
maxx = float("-inf")
for i in range(0, len(s) - 1, 2):
	l1 = s[i]
	l2 = s[i + 1]
	if l1 + l2 == "XA":
		count += 1
		maxx = max(maxx, count)
	else:
		count = 0
print(maxx)