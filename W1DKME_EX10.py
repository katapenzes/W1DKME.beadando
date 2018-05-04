import math
def EX10():
    s = math.factorial(20)
    for i in range(1,s):
        db = 0
        for j in range(1,21):
            if i%j==0:
                db += 1
        if db == 20:
            return i

print(EX10())


