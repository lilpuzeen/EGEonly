print("y y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not(((x <= y ) and (y <= w)) or (z == ( x or y))):
                    print(x, y, w, z)
