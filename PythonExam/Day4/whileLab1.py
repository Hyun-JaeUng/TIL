import random

num = random.randint(5,10)
a = 1

while a<=num:
    print(a,"->",a**2)
    a+=1

# while은 조건이 True일 때까지 계속 실행