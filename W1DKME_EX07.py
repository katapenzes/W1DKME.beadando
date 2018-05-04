def EX7():
    x = input("Adj meg egy mondatot:")
    t = []
    for i in x.split(' '):
        if i == i[::-1]:
            t.append(i)
    min = 0
    for j in t:
        if len(j)>min:
            a = j
    return a


print(EX7())

