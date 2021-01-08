def sumEven1(*n):
    sum = 0
    if len(n) == 0:
        sum = -1
    else:
        for i in range(len(n)):
            if n[i] >= 1:
                if n[i] % 2 == 0:
                    sum += n[i]
            else:
                sum = -1
                break
    return sum

print(sumEven1(1,2,3,4,5,6))
print(sumEven1(1,3,5))
print(sumEven1(1,132,5,1088,2))
print(sumEven1())
print(sumEven1(1,5,6,0))

# len을 활용하기

