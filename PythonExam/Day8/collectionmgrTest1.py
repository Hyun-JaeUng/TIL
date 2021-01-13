score = [ 88, 95, 70, 100, 99 ]
for no, s in enumerate(score, 1):
    print(str(no) + "번 학생의 성적 :", s)

names = "둘리,고길동,희동이,마이콜,또치,도우너"
namelist = names.split(",") # 리스트 생성
print(namelist)
namelist.sort()
for num, name in enumerate(namelist) :
    print(f"이름순으로 {name}는 {num+1}번입니다.") # f string 사용
for data in enumerate(namelist) :
    print(f"enumerate를 적용한 결과 : {data}") # enumerate에서 언패킹한게 아니라 한 개 변수이기에 튜플로 들어옴 (언패킹 안된다 생각)
for num, name in enumerate(namelist, 100) : # 인덱스 숫자 시작, 기본값 0
    print(f"이름순으로 {name}는 {num}번입니다.")




