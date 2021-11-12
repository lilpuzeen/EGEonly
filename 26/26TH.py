file = open("27884.txt", "r")
S = int(file.readline())
summ, cnt, check = 0, 0, []

nums = sorted([int(rows) for rows in file.readlines()])
unique = set(nums)

for num in nums:
    if summ + num <= S:
        summ += num
        cnt += 1
        check.append(num)
    else:
        break

for item in unique:
    check[len(check)-1] = item
    if sum(check) <= S:
        continue
    else:
        result = item-1
        break

print(cnt, result)
file.close()
