def func1(n) :
    return n * 2

def func2() :
    print("func2 호출 - hello")

print(type(func1))
print(type(func2))
print(func1(10))
print(func2()) # 함수 안 실행하고, 리턴값은 없는 함수라 None 프린트됨

print("=" * 20)
print(func2)
v = func2 # 함수 자체를 넣기위해서는 가로를 빼고 넣어야함. 그래야 리턴값이 아닌 함수가 변수에 저장
print(v)
v()

def say1() :
    print("안녕?")

def say2() :
    print("Hello?")

print("=" * 20)
import types
def callback(fn) :
    if type(fn) == types.FunctionType : #키워드가 없는거라 types을 import 함
        fn() # 그 아규먼트인 함수를 실행해라!
    else :
        print("아규먼트로 함수를 주세요")

callback(say1)
callback(say2)
callback(100)



