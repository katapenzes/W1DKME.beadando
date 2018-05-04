def EX4(str):
    t = ''
    str = str.lower()
    for i in str.split(' '):
        for j in range(1,len(i)):
            t += i[j]
        t += i[0]
        t += 'ay'
        t += ' '
    return t.capitalize()




print(EX4('The quick brown fox'))
