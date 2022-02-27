file = open("17.txt")
count = 0
arr = [int(x) for x in file.readlines()]
for i in range(len(arr)):
    try:
        if (str(arr[i]).endswith("9")) and (arr[i] > 0) and (str(arr[i-1]).endswith("9") is False) and (str(arr[i+1]).endswith("9") is False):
            print(arr[i - 1], arr[i], arr[i+1])
            count += 1
    except IndexError:
        print("!!!!!!!!!!!!Exception!!!!!!!!!!!!!")
        print(i, arr[i])
print(count)
