import math
def EX3(str):
    x = '*'
    max = -(math.inf)
    for i in str:
        if len(i) > max:
            max = len(i)
    print((max+4)*x)
    for j in str:
        j += (max-len(j))*' '
        print("{0} {1} {2}".format(x,j,x))
    print((max+4)*x)



a = ["Hello", "World", "in", "a", "frame"]
print(EX3(a))
