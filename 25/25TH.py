############# Задание 25 №27851 #############
from pprint import pprint
line = [x for x in range(174457, 174505)]
divlist = []
memory = []

for i in line:
    for divider in range(2, 174505):
        if len(memory) == 2:
            t = (tuple(memory[:]))
            divlist.append(t)
            memory = []
            break
        if i % divider == 0:
            if divider == i:
                continue
            else:
                memory.append(divider)
                continue
pprint(divlist)


# for x in line:
#     for k in range(1, 245757):
#         if len(memory) == 2:
#             t = (tuple(memory[:]))
#             a = t[1] if t[1] > 245690 else False
#             try:
#                 divlist.append((line.index(a) + 1, a))
#             except Exception:
#                 pass
#             memory = []
#             break
#         if x % k == 0:
#             memory.append(k)
#             continue

# print(divlist)