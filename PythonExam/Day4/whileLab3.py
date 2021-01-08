import random

num = random.randint(0,30)
count = 0

while True:
    if num>= 27 or num == 0:
        print("수행횟수는",count,"번입니다.")
        break
    else:
        print(chr(64+num),"(" + str(num) + ")")
        count += 1
        num = random.randint(0, 30)

# 대문자 chr(65) = A 이후 순서대로 증가
# 소문자 chr(97) = a 이후 순서대로 증가
