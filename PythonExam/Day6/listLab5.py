import random
x = []

while True:
    x.append(random.randint(1,45))
    ans = list(set(x))
    if len(ans) == 6:
        break

ans.sort()
print("행운의 로또번호 :", ans)


