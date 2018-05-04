def EX8():
    a = input('Első szó:')
    b = input('Második szó:')
    m = ''
    for i in a:
        for j in b:
            if i == j:
                m += j

    if m == '':
        return None
    return m



print(EX8())
