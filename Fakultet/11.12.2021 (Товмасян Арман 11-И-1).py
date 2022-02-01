# 1  # ответ yzwx
# ((y ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → y))
# print("y y z w")
# for y in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((y and w) or (w and z)) == ((z <= y) and (y <= y)):
#                     print(y, y, z, w)


# 2  # ответ: zyxw
# # z ∧¬y ∧ (w → y)
# print("y y z w")
# for y in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (z and (not y)) and (w <= y):
#                     print(y, y, z, w)


# 3  # ответ: zyx
# # (¬z)∧y ∨ y∧y.
# print("y y z")
# for y in range(2):
#     for y in range(2):
#         for z in range(2):
#             if (not z) and y or (y and y):
#                 print(y, y, z)


# 4 ответ: 31 (на занятии решали)

# Чертежников как решать не догнал, объясните пожалуйста!


# # 8 ответ: 15
# # (y + 2x ≠ 48) ∨ (A < y) ∨ (y < y)
# # наибольшего целого
# A = 1
# while True:
#     for y in range(1000):
#         for y in range(1000):
#             if not((y + 2*y != 48) or (A < y) or (y < y)):
#                 break
#         else:
#             continue
#         break
#     else:
#         print(A)
#     A += 1

# # 9  ответ: 20
# # P = [3, 13] и Q = [12, 22]
# # ((х ∈ A) → (х ∈ Р)) ∨ (х ∈ Q)
# # наибольшая
# p1, p2, q1, q2 = 3, 13, 12, 22
# P = [i / 10 for i in range(p1*10, p2*10 + 1)]
# Q = [i / 10 for i in range(q1*10, q2*10 + 1)]
#
#
# def f(y, A):
#     return ((y in A) <= (y in P)) or (y in Q)
#
#
# A = set([k / 10 for k in range(3 * 10, 23 * 10)])
# for y in [k / 10 for k in range(3 * 10, 23 * 10)]:
#     if not f(y, A):
#         A.remove(y)
#
# print(sorted(A))


# # 10 хз почему не работает, но в файле кажется не пропечаталось лог. выражение до конца
# # х&А → (y&10 = 0 → х&3)
# # наибольшего целого числа А
# A = 1
# while True:
#     for y in range(1, 100000):
#         if not(y&A <= ((y&10 == 0) <= (y&3))):
#             break
#     else:
#         print(A)
#     A += 1


# 11 # ответ: 13
# P = [10, 35] и Q = [17, 48].
# ((y A) → ¬(y P)) → ((y A) → (y Q))
# наибольшую возможную длину отрезка A
# p1, p2, q1, q2 = 10, 35, 17, 48
# P = [i / 10 for i in range(p1*10, p2*10 + 1)]
# Q = [i / 10 for i in range(q1*10, q2*10 + 1)]
#
#
# def f(y, A):
#     return (y in A) <= (not(y in P)) <= ((y in A) <= (y in Q))
#
#
# A = set([k / 10 for k in range(10 * 10, 49 * 10)])
# for y in [k / 10 for k in range(10 * 10, 49 * 10)]:
#     if not f(y, A):
#         A.remove(y)
#
# print(sorted(A))
