mul = 1

while True:
    num = int(input("숫자를 입력하세요. :"))
    if num ==0:
        print("종료")
        break
    elif num > 10 or num < -10:
        continue
    elif num > 0:
        print("입력값 :", num)
        mul *= num
        print(mul)
    else:
        print("입력값(부호변경) :", -num)
        mul *= (-num)
        print(mul)



