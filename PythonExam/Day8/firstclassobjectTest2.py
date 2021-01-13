# 함수 안에 함수 정의, exp는 함수 안에서만 호출가능
def fct_fac(n) :
    def exp(x) :
        return x**n
    return exp

rtnf1 = fct_fac(2) # 둘 다 함수가 들어온 것
rtnf2 = fct_fac(3)

print(type(rtnf1)) # function 타입이다.
print(type(rtnf2))

print(rtnf1(4))
print(rtnf2(4))
print(fct_fac(2)(5))
print(fct_fac(5)(3))
