# finally에서 오류나지 않도록 None 값 대입
f = None
try:
    # 파일 열기 및 대소문자 구분하지 않고 카운트하기 위해 lower() 이용
    f = open("yesterday.txt", "rt", encoding="UTF-8")
    ans = 0
    for i in f:
        ans += i.lower().count("yesterday")

except FileNotFoundError:
    print("파일을 읽을 수 없어요.")
else:
    print("Number of a Word \'Yesterday\'", ans)
finally:
    print("수행완료!!")
    # open시 오류가 났을 때, 실행되는 finally 구문에서 오류가 다시 나지 않도록 방지하기 위한 코드
    if f:
        f.close()

