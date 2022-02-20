for i in range(101, 1000):
    n = bin(i)[2:]
    counts = {"0": n.count("0"),
              "1": n.count("1")}
    if counts["0"] == counts["1"]:
        n += n[-1]
    else:
        n += min(str(counts.values()))

    if counts["0"] == counts["1"]:
        n += n[-1]
    else:
        n += min(str(counts.values()))

    if (int(n, 2) % 2 == 0) and (int(n, 2) % 4 != 0):
        print(i)


