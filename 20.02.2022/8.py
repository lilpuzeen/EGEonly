count = 0
m = ['16', '61', '36', '63', '56', '65', '76', '67', '69', '96']
for i in range(4096, 32767+1):
    s = oct(i)[2:]
    if s.count("6") == 1 and all(x not in s for x in m):
        count += 1
print(count)
