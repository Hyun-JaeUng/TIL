yoil = ["월", "화", "수", "목","금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겹살"]
menu = zip(yoil, food)
print(menu, type(menu)) #type이 , zip 객체임
for y, f in menu:
    print("%s요일 메뉴 : %s" % (y, f))

print("*"*20)
menu = zip(yoil, food)
d2 = dict(menu) # 딕셔너리로
for y, f in d2.items():
    print("%s요일 메뉴 : %s" % (y, f))
print(d2)
print(menu)

print("*"*20)

zip1 = zip([1, 2, 3], [4, 5, 6])
zip2 = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
zip3 = zip("abc", "def")


#print(list(zip1))
print(list(zip2))
print(list(zip3))
print("이거는 왜 비어있을까?")
print(dict(zip1))
print(dict(zip3))
