class Book:
    # 아규먼트 설정 및 멤버 변수 초기화 메서드
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = int(price)

    # 하나의 문자열로 return 받기 위한 f-string
    def getBookInfo(self):
        return f"{self.title},{self.author},{self.price}"

# 객체 생성
b1 = Book("파이썬정복", "김상형", 28000)
b2 = Book("이것이 MariaDB다", "우재남", 30000)
b3 = Book("파이썬 웹프로그래밍", "김석훈", 22000)
b4 = Book("맛있는 MongoDB", "정승호", 28000)
b5 = Book("생활코딩! HTML+CSS+자바스크립트", "이고잉", 27000)

# replace를 이용한 함수의 리턴값 출력
for i in [b1, b2, b3, b4, b5]:
    print(i.getBookInfo().replace(',',"\n"))
    print('-'*20)


