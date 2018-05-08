import numpy as np

t = np.empty(8, dtype='object')
szamok = np.empty(9, dtype='object')
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            for l in range(0,3):
                for m in range(0,3):
                    for n in range(0,3):
                        for o in range(0,3):
                            for p in range(0,3):
                                t[0] = i
                                t[1] = j
                                t[2] = k
                                t[3] = l
                                t[4] = m
                                t[5] = n
                                t[6] = o
                                t[7] = p

                                meret = 0
                                szamok[0] = 1
                                for r in range(0,8):
                                    if t[r] == 0:
                                        meret += 1
                                        szamok[meret] = r+2
                                    elif t[r] == 1:
                                        meret += 1
                                        szamok[meret] = -r-2
                                    elif t[r] == 2:
                                        szamok[meret] = szamok[meret]*10
                                        if szamok[meret] > 0:
                                            szamok[meret] = szamok[meret]+r+2
                                        else:
                                            szamok[meret] = szamok[meret]-r-2



                                szum = 0
                                for r in range(0,meret+1):
                                    szum += szamok[r]
                                if szum == 100:
                                    s = ''
                                    s += str(szamok[0])
                                    for r in range(1,meret+1):
                                        if szamok[r] > 0:
                                            s += '+'
                                        s += str(szamok[r])
                                    s += ' = 100'
                                    print(s)
















