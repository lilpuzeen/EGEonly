a = 1
while True:
<<<<<<< HEAD
    for x in range(100):
        for y in range(100):
            if not((2*x + 3*y > 30) or (x + y <= a)):
                break
        else:
            continue
        break
    else:
        print(a)
    a += 1

=======
	for x in range(1000):
		for y in range(1000):
			if not((2*x + 3*y > 30) or (x + y <= a)):
				break
		else:
			continue
		break
	else:
		print(a)
	a += 1
>>>>>>> df8a5e3 (macbook 16.06.2022 / brand new game theory)
