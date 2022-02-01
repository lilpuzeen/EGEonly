def p(x):
    return x > 1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))


if __name__ == '__main__':
    for i in range(245690, 245756+1):
        if p(i):
            print(i - 245690 + 1, i)
