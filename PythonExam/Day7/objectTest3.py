import datetime

print([4,15,2,30,4].count(4))
listv = [4,15,2,30,4]
print(listv.count(4))

now = datetime.date.today()
print(now, type(now))
print(now.weekday()) # 화요일 - 1
print(now.ctime())
print("===2021년 크리스마스===")
christmas = datetime.date(2021, 12, 25)
print(christmas, type(christmas))
print(christmas.weekday()) # 토요일 - 5
print(christmas.ctime())
