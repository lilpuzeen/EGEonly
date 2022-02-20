s = "АБВГД БВЕ ВЕЖЗ ГЗВ ДЗГ ЕЖИ ЖИ ЗЖИ ИКЛ КМ ЛМ М"
d = {w[0]: w[1:] for w in s.split()}
f = lambda a, b: (a == b) + sum(f(c, b) for c in d[a])
print(f("А", "В") * f("В", "М"))
