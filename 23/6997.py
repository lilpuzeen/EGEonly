def tr(start, finish):
	if start > finish:
		return 0
	if start == finish:
		return 1
	return tr(start + 1, finish) + tr(start * 2, finish) + tr(start*2 + 1, finish) + tr(start * 10, finish)

print(tr(1, 15))