import random

x = random.randint(1,10)
y = random.randint(30,40)
sum = 0

for i in range(x,y+1):
    if i%2 == 0:
        sum += i

print(x," 부터 ",y," 까지의 짝수의 합 :", sum)
