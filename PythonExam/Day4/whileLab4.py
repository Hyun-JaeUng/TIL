
while True:
    num = int(input("월을 입력하세요. : "))
    season =" "
    if num>=1 and num <=12:
        if num == 12 or num <= 2:
            season = "겨울"
        elif num <= 5:
            season = "봄"
        elif num <= 8:
            season = "여름"
        else:
            season = "가을"
        print(num, "월은", season)
    else:
        print("1~ 12 사이의 값을 입력하세요!")
        break
