def EX11():

    for i in range(100,1000):
        for j in range(100,1000):
            s = i*j
            if str(s) == str(s)[::-1]:
                x = str(s)
                a = i
                b = j
    return '{0} * {1} = {2}'.format(a,b,x)


print(EX11())
