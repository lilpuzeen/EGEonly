def tr(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start == 15:
        return 0
    return tr(start + 1, end) + tr(start + 2, end)


print(tr(3, 9) * tr(9, 20))
