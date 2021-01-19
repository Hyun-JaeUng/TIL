# 클래스 생성
class Member :
    # 아규먼트로 받지 않는 멤버변수 만들고, 기본값 None으로 설정
    def __init__(self):
        self.name = None
        self.account = None
        self.passwd = None
        self.birthyear = None

# 3개의 객체(인스턴스) 생성
m1 = Member()
m2 = Member()
m3 = Member()

# 생성된 객체의 각 멤버 변수 저장 및 세팅
m1.name = "현재웅"
m1.account = "미래웅"
m1.passwd = 1234
m1.birthyear = 605

m2.name = "황영민"
m2.account = "squeaky"
m2.passwd = 1235
m2.birthyear = 1125

m3.name = "홍혜림"
m3.account = "브라운팜"
m3.passwd = 7896
m3.birthyear = 1121


print(f"회원1 : {m1.name}({m1.account}, {m1.passwd}, {m1.birthyear})")
print(f"회원2 : {m2.name}({m2.account}, {m2.passwd}, {m2.birthyear})")
print(f"회원3 : {m3.name}({m3.account}, {m3.passwd}, {m3.birthyear})")

# 아규먼트를 설정하지 않고, 이렇게 코딩하면 각각 세팅해야해서 굉장히 불편함!
