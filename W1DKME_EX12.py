def is_prime(num):


    if num==2:
            return 'Prime'
    for i in range(2,num):
        if num%i == 0:
            return 'Not Prime'
    return 'Prime'



def EX12():
    m = []
    m.append(1)
    i = 1
    j = 2
    while True:
        if i==10001:
            return m[i-1]
        elif is_prime(j) == 'Prime':
            m.append(j)
            i += 1
        j += 1



print(EX12())

