import os

# 경로 설정 - 파이썬에서 \는 escape문 떄문에 두번 연속 해야함, 또 c뒤에 : 붙이는거 생각
if not os.path.isdir('C:\\iotest'):
    os.mkdir('C:\\iotest')
ans_txt = open("C:\\iotest\\today.txt", "wt", encoding="UTF-8")
ans_txt.write("""오늘은 2021년 01월 18일입니다. 
오늘은 월요일입니다. 
나는 현재요일에 태어났습니다.
화이팅!""")
ans_txt.close()
print("저장이 완료되었습니다.")

