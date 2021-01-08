
def differtwovalue(x1,x2):
    if x1 >= x2:
        ans = x1 - x2
        print(x1,"와",x2,"의 차는",ans,"입니다.")
        return ans
    else:
        ans = x2 - x1
        print(x2, "와", x1, "의 차는", ans, "입니다.")
        return ans
    # return은 보통 1번! 코드 양 줄이는 것이 맞음

import random

for i in range(1,6):
    a = random.randint(1,30)
    b = random.randint(1,30)
    differtwovalue(a,b)
