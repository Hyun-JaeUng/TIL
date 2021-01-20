import calendar

# while문을 밖에 해야 에러가 났을 시 멈추지 않고, 다시 try 코드 실행
while True:
    try:
        a = int(input("년도와 월을 숫자로 입력해주세요. ex)yyyymm: "))
        year = a//100
        month = a%100
        print(calendar.month(year, month))
        break
    # 에러메시지를 저장하여 함께 출력하는 형태로 코딩
    except ValueError as v:
        print("입력값이 잘못되었습니다.(" + str(v) + ")")
