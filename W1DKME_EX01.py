def EX1():
    szum = 0
    x = 1
    y = 1
    print(x)
    print(y)
    for i in range(98):
        szum = x + y
        print(szum)
        x = y
        y = szum


print(EX1())
