import random
x = set()

while True:
    x.add(random.randint(1,45))
    if len(x) == 6:
        break

print("행운의 로또 번호 :", x)
