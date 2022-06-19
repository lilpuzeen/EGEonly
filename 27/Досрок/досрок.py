# A - 471228
# B - 49113954961677
f = open("107_27_A.txt")
n = int(f.readline())
arr = [3*int(x) for x in f.readlines()]

minn = float("inf")
s = [0]*n

for i in range(n):
	r = min(n - i, i)
	s[0] += r * arr[i]

left = sum(arr[n//2:])
right = sum(arr[:n//2])
sr = arr[n//2]

for i in range(1, n):
	left = left + arr[i] - arr[(i + n//2) % n]
	right = right - arr[i] + arr[(i + n//2) % n]
	s[i] = s[i-1] + left - right

print(min(s))