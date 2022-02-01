def tr(start, finish):
    if start > finish:
        return 0
    if start == finish:
        return 1
    if start == 17:
        return 0
    return tr(start+1, finish) + tr(start*2, finish)


print(tr(1, 10)*tr(10, 21))
