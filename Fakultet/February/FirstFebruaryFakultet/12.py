s = "9" * 1000

while ("999" in s) or ("888" in s):
    if "888" in s:
        s = s.replace("888", "9", 1)
    else:
        s = s.replace("999", "8", 1)

print(s)
