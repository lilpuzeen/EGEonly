def binary_search(array, element, start, end):
    if start > end:
        return -1
    mid = (start + end)//2
    if element == array[mid]:
        return mid
    if element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)


f = open("26_1var.txt", "r+")
arr = [int(x) for x in f.readlines()]
arr = sorted(arr)
count = 0
maxmiddle = -10000
for i in range(len(arr)-1):
    if arr[i] % 2 == 0:
        for x in range(i + 1, len(arr)):
            if arr[x] % 2 == 0:
                middle = (arr[i] + arr[x]) // 2
                if binary_search(arr, middle, i, x):
                    count += 1
                    if middle > maxmiddle:
                        maxmiddle = middle
print(count, maxmiddle)
