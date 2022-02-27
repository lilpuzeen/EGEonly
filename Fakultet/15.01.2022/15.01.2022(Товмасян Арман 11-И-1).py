def calc(x: int, a: int, b: int) -> str:
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


# # 6
# print(bin(8**5 + 4**6 + 2**12 - 16)[2:].count("1"))  # Ответ: 10

# # 7
# print(bin(16**2018 + 4**2018 + 25 - 1)[2:].count("1"))  # Ответ: 4

# # 8
# print(bin(4**2016 + 2**2015 - 7)[2:].count("1"))  # Ответ: 2014

# 9 Ответ: 4
# k = 216**6 + 216**4 + 36**6 - 6**14 - 24
# print(len(set(str(calc(k, 10, 6)))))

# 10 Ответ: 15
# k = 3 * 4**38 + 2 * 4**23 + 4**20 + 3 * 4**5 + 2 * 4**4 + 1
# print(hex(k)[2:].count("0"))

# 11 Ответ: 14
# k = 6 * 343**5 + 5 * 49**7 - 50
# print(calc(k, 10, 7).count("6"))

# 12 Ответ: 13
# k = 125**5 + 25**9 - 30
# print(calc(k, 10, 5).count("4"))

# 13
# print(bin(4**511 + 2**511 - 511)[2:].count("1"))  # Ответ: 504

# 14 Ответ: 393
# for x in range(1, 100000):
#     i = x
#     L = 0
#     M = 0
#     while x > 0 :
#         M = M+1
#         if (x % 2) != 0:
#             L = L + x % 8
#         x = x // 8
#     if L == 2 and M == 3:
#         print(i)

# 15 Ответ: 219
# for x in range(100000):
#     i = x
#     a = 0; b = 0
#     while x > 0:
#         if x % 2 == 0:
#             a += 1
#         else:
#             b += x % 6
#         x = x // 6
#     if a == 2 and b == 4:
#         print(i)