arr = [int(x) for x in input().split()]


maxx = max(arr)
minn = min(arr)
ind_max = arr.index(maxx)
ind_min = arr.index(minn)

arr[ind_min], arr[ind_max] = arr[ind_max], arr[ind_min]

print(*arr)
