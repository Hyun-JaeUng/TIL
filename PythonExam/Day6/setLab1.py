import random
x =set() # 빈 세트는 이 방법 뿐
y =set()

# 난수 추출하여 저장
while True:
    x.add(random.randint(1,20))
    if len(x) == 10:
        break
while True:
    y.add(random.randint(1,20))
    if len(y) == 10:
        break

print("집합 1 :", x)
print("집합 2 :", y)
print("합 집합", x|y)
print("집합 1 - 집합 2 차집합 :", x-y)
print("집합 2 - 집합 1 차집합 :", y-x)
print("집합 1과 2가 각자 가지고 있는 데이터 :", x^y)


