def tr(start, finish):
    if start > finish:
        return 0
    if start == finish:
        return 1
    if start == 14:
        return 0
    return tr(start+1, finish) + tr(start+2, finish)


print(tr(2, 9)*tr(9, 18))
