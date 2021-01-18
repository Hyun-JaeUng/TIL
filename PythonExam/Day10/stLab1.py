try:
    import calendar
    while True:
        a = int(input("년도와 월을 숫자로 입력해주세요. ex)yyyymm: "))
        year = a//100
        month = a%100
        print(calendar.month(year, month))
        break
except ValueError:
    print("숫자를 입력해주세요.")
