def tr(start, finish):
    if start > finish:
        return 0
    if start == finish:
        return 1
    return tr(start * 2, finish) + tr(start * 3, finish)


a = tr(2, 16)
