s = "8"*70
print("2222" in s)
while ("2222" in s) or ("8888" in s):
    if "2222" in s:
        s = s.replace("2222", "88")
    else:
        s = s.replace("8888", "22")
print(s)
