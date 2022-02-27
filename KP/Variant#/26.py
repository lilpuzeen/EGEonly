file = open("26.txt", "r+")
n = 1000
k = 50
arr = [int(x) for x in file.readlines()]
arr = sorted(arr)
arr = arr[k:len(arr) - k]
print(arr)
print(max(arr), (sum(arr) / len(arr)))
