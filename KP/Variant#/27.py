n = 20
file = open("27.txt", "r+")
arr = [list(map(int, x.split())) for x in file.readlines()]

