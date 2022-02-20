def tr(start, finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    return tr(start + 1, finish) + tr(start + 2, finish) + tr(start * 2, finish)


print(tr(3, 10) * tr(10, 12))
