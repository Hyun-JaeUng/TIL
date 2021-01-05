import random

oper_num = random.randint(1,10)
a = 300
b = 50

if oper_num == 1 or oper_num == 6:
    ans = a+b
elif oper_num == 2 or oper_num == 7:
    ans = a-b
elif oper_num == 3 or oper_num == 8:
    ans = a*b
elif oper_num == 4 or oper_num == 9:
    ans = a/b
else:
    ans = a%b

print("결과값 : ", ans)

