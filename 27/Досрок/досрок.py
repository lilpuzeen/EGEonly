f = open("107_27_A.txt")
n = int(f.readline())
arr = [int(x) for x in f.readlines()]

minn = float("inf")
s = [0]*n

for i in range(len(arr)):
	for j in range(len(arr)):
		r = min(abs(i - j), n-abs(i-j))
		s[i] += 3*r*arr[j]
print(min(s))