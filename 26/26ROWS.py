file = open("26.txt", "r")
n = int(file.readline())
nums = []
for item in file.readlines():
    place = list(map(int, item.split()))
    nums.append(place)
nums.sort()
row, seat = 0, 0
for i in range(len(nums)):
    if nums[i][0] == nums[i-1][0]:
        if nums[i][1] - nums[i-1][1] == 3:
            r = nums[i][0]
            m = -nums[i][1] + 2
print(r, abs(m))

# file = open("26.txt", "r")
# n = int(file.readline())
# nums = []
# for x in range(n):
#     pair = list(map(int, file.readline().split()))
#     pair[1] = -pair[1]
#     nums += [pair]
# nums.sort()
# row, seat = 0, 0
# for x in range(len(nums)):
#     if nums[x][0] == nums[x-1][0]:
#         if nums[x][1] - nums[x-1][1] == 3:
#             r = nums[x][0]
#             m = -nums[x][1] + 1
# print(r,m)
