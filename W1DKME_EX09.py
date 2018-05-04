def is_prime(number):

    if number==2:
            return 'Prime'
    for i in range(2,number):
        if number%i == 0:
            return 'Not Prime'
    return 'Prime'



def EX9(num):
    m = []
    k = []
    for i in range(2,num):
        if num%i==0:
            m.append(i)

    for i in m:
        if is_prime(i)=='Prime':
            k.append(i)
    max = 0
    for j in k:
        if j>max:
            max = j
    return max


print(EX9(600851475143))
