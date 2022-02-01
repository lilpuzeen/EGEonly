def tr(start, finish):
    if start > finish:
        return 0
    if start == finish:
        return 1
    if start == 12:
        return 0
    return tr(start+1, finish) + tr(start+2, finish) + tr(start*3, finish)


print(tr(2, 9)*tr(9, 19))
