# 1  # ответ yzwx
# ((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x))
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and w) or (w and z)) == ((z <= y) and (y <= x)):
#                     print(x, y, z, w)


# 2  # ответ: zyxw
# # z ∧¬y ∧ (w → x)
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (z and (not y)) and (w <= x):
#                     print(x, y, z, w)


# 3  # ответ: zyx
# # (¬z)∧x ∨ x∧y.
# print("x y z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if (not z) and x or (x and y):
#                 print(x, y, z)


# 4 ответ: 31 (на занятии решали)

# Чертежников как решать не догнал, объясните пожалуйста!


# # 8 ответ: 15
# # (y + 2x ≠ 48) ∨ (A < x) ∨ (x < y)
# # наибольшего целого
# A = 1
# while True:
#     for x in range(1000):
#         for y in range(1000):
#             if not((y + 2*x != 48) or (A < x) or (x < y)):
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
# def f(x, A):
#     return ((x in A) <= (x in P)) or (x in Q)
#
#
# A = set([k / 10 for k in range(3 * 10, 23 * 10)])
# for x in [k / 10 for k in range(3 * 10, 23 * 10)]:
#     if not f(x, A):
#         A.remove(x)
#
# print(sorted(A))


# # 10 хз почему не работает, но в файле кажется не пропечаталось лог. выражение до конца
# # х&А → (x&10 = 0 → х&3)
# # наибольшего целого числа А
# A = 1
# while True:
#     for x in range(1, 100000):
#         if not(x&A <= ((x&10 == 0) <= (x&3))):
#             break
#     else:
#         print(A)
#     A += 1


# 11 # ответ: 13
# P = [10, 35] и Q = [17, 48].
# ((x A) → ¬(x P)) → ((x A) → (x Q))
# наибольшую возможную длину отрезка A
# p1, p2, q1, q2 = 10, 35, 17, 48
# P = [i / 10 for i in range(p1*10, p2*10 + 1)]
# Q = [i / 10 for i in range(q1*10, q2*10 + 1)]
#
#
# def f(x, A):
#     return (x in A) <= (not(x in P)) <= ((x in A) <= (x in Q))
#
#
# A = set([k / 10 for k in range(10 * 10, 49 * 10)])
# for x in [k / 10 for k in range(10 * 10, 49 * 10)]:
#     if not f(x, A):
#         A.remove(x)
#
# print(sorted(A))
