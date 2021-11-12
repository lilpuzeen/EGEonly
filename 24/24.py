file = open("inf_22_10_20_24.txt", "r+")
arr = [str(x) for x in file.readlines()]
counter = 0
for item in arr:
    if item.count("E") > item.count("A"):
        counter += 1

print(counter)
