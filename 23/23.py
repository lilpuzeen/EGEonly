def tr(start, finish):
    if start > finish:
        return 0
    if start == finish:
        return 1
    if start == 29:  # Исключаем числа, по которым не должны пройтись
        return 0  #
    return tr(start + 1, finish) + tr(start * 2, finish) + \
           tr(start * 3, finish)  # Пишем все возможные комбинации ходов


if __name__ == '__main__':
    print(tr(5, 68) * tr(68, 102))  # Декартово произведение
