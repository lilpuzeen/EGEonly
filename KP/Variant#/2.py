def tr(start, finish):
    if start > finish:
        return 0
    if start == finish:
        return 1
    return tr(start + 1, finish) + tr(start * 1.5, finish) if ((tr(start * 1.5, finish)) % 2 == 0) else tr(start + 1, finish)


a = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
b = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
c = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"
d = "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"
print(len(a), len(b), len(c), len(d))