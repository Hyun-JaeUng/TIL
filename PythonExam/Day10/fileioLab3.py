try:
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
