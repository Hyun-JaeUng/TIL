def calc():
    num  = 100
    return lambda : num + 1    # 람다 표현식을 반환
# 리턴값에서 쓰인 함수의 지역변수는 계속 유지됨 - 클로저

c1 = calc()
print(calc()())
print(c1(), c1(), c1())


def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환

c2 = calc()
print(c2(1), c2(2), c2(3), c2(4), c2(5))

# 아우터 함수와 이너 함수(expr)
def calc():
    a = 3
    b = 5
    def expr(x) :
        return a * x + b

    return expr
# 리턴값으로 쓰여서 이너함수가 계속 유지됨
c3 = calc()
print(c3(100), c3(200), c3(300), c3(400), c3(500))
print(calc()(100))

