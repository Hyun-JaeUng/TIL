dic = {'월':(-12,-3),'화':(-4,2),'수':(-8,8),'목':(-3,5),
       '금':(-7,7),'토':(-13,-3),'일':(-6,-2)}

day = input("요일명을 한글로 입력하세요: ")

if day in dic.keys():
    print(day,"요일의 최저온도는", dic[day][0], "이고 최고 온도는", dic[day][1], "입니다." )
else:
    print(day, "요일의 정보를 찾을 수 없습니다.")

