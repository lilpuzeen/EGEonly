print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not((not(w <= z)) or (x <= y) or (not x)):
                    print(x, y, w, z)
# wzyx