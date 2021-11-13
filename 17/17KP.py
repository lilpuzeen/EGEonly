a = [int(x) for x in open("17kp.txt").readlines()]
mid = sum(a) // len(a)
count, minn = 0, 10**10
try:
    for i in range(len(a)):
        if ((a[i] < mid) or (a[i + 1] < mid)) and (("4" not in str(a[i])) and ("4" not in str(a[i + 1]))):
            if a[i] + a[i + 1] < minn:
                minn = a[i] + a[i + 1]
            count += 1
except IndexError:
    print(count, minn)
