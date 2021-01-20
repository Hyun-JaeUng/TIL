import os
import time
import calendar

now = time.localtime()
week = ['월', '화', '수', '목', '금', '토', '일']

# 디렉터리의 존재여부 체크 및 없다면 폴더 생성 (경로 설정 주의)
if not os.path.isdir('C:\\iotest'):
    os.mkdir('C:\\iotest')

# today.txt가 없다면 생성하고, 쓰기(write) 모드로 열기
ans_txt = open("C:\\iotest\\today.txt", "wt", encoding="UTF-8")

# f-string과 time 모듈을 이용한 출력
ans_txt.write(f"""오늘은 {now.tm_year}년 입니다. 
오늘은 {week[calendar.weekday(now.tm_year, now.tm_mon, now.tm_mday)]}요일 입니다. 
나는 {week[calendar.weekday(1996,6,5)]}요일에 태어났습니다.
화이팅!""")

# open 파일 close 해주기
ans_txt.close()
print("저장이 완료되었습니다.")


