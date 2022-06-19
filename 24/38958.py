s = open("38958.txt").readline()
count = 0
countA = 0
maxx = float("-inf")
for i in range(len(s)):
	if s[i] == "A":
		ind = i
		countA += 1
		count += 1
