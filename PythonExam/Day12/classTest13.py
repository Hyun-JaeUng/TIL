class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __str__(self):
        return "이름 %s, 나이 %d" % (self.name, self.age)
    def __len__(self):
        return self.age

kim = Human(29, "김상형")
print(kim)
print(len(kim))

# 특수 메서드가 있어서 클래스에서 정의한 그 len 함수가 실행된 결과를 볼 수 있음