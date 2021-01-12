import time
def gettime():
    now = time.localtime()
    print(now, type(now))
    return now.tm_hour, now.tm_min # 자동으로 패킹되어 튜플로 리턴됨

result = gettime()
print("지금은 %d시 %d분입니다" % (result[0], result[1]))

hour, minute = gettime()
print("지금은 %d시 %d분입니다" % (hour, minute))

# =============== divmod  ===============
d, m = divmod(7, 3)  # 파이썬 내장함수
print("몫", d)
print("나머지", m)