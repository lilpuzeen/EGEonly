s = "АБВГ БДВ В ГИ ДЖКЕ ЕИК ИК ЖК КЛМН ЛН МН Н"
d = {w[0]: w[1:] for w in s.split()}
f = lambda a, b: (a == b) + sum(f(c, b) for c in d[a])
print(f("А", "Н"))
