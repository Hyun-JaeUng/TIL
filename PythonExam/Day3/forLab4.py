evenNum = 0
oddNum = 0

for i in range(1,101):
    if i%2 == 1:
        oddNum += i
    else:
        evenNum +=i

print("1부터 100까지의 숫자들 중에서 \n짝수의 합은 ", evenNum,"이고 \n홀수의 합은 ",oddNum,"이다." )

