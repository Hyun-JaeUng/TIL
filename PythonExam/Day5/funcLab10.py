def sumAll(*n):
    sum = 0
    count = 0
    for i in n:
        if type(i) == int or type(i) == float:
            sum += i
            count+=1

    if len(n) == 0 or count == 0:
        sum = None

    return sum
print(sumAll(1,2,3,4,5,100))
print(sumAll(5,6,"dd",3.14))
print(sumAll())
print(sumAll("zz", "zz"))
print(sumAll(0,0))

