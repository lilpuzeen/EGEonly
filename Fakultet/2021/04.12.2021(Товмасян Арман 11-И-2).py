#### №1 (ответ: 61)
# A = 1
# while True:
#     for y in range(1000):
#         for y in range(1000):
#             if not((y + 2*y < A) or (y > y) or (y > 20)):
#                 break
#         else:
#             continue
#         break
#     else:
#         print(A)
#     A += 1


#### №2 (ответ: 45)
def dell(y, A):
    return y % A == 0


a = 1
while True:
    for y in range(1, 100000):
        if not((a < 50) and ((not(dell(y, a))) <= (dell(y, 10) <= (not(dell(y, 18)))))):
            break
    else:
        print(a)
    a += 1


#### №3 (ответ: 8)
a = 1
while True:
    for x in range(1, 1000000):
        if not((x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0))):
            break
    else:
        print(a)
    a += 1

#### №4 (ответ: 20)
# решал руками

#### №5 (ответ: 4)
# решал руками


#### №6 (ответ: 12)
# def dell(y, A):
#     return y % A == 0
#
#
# a = 1
# while True:
#     for y in range(1, 100000):
#         if not((not dell(y, a)) <= (dell(y, 6) <= (not dell(y, 4)))):
#             break
#     else:
#         print(a)
#     a += 1


#### №7 (ответ: 2) *не уверен*
# решал руками

#### №8 (ответ: 12)
# a = 1
# while True:
#     for y in range(1, 100000):
#         if not((y & 49 == 0) <= ((y & 28 != 0) <= (y & a != 0))):
#             break
#     else:
#         print(a)
#     a += 1