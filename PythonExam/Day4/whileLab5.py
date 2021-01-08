
while True:
    word = input("문자열을 입력하세요. : ")
    wordlength = len(word)
    if wordlength == 0:
        break
    elif 5<= wordlength <= 8:
        continue # 반복문에서 이번 작은 반복을 넘긴다.
    elif wordlength < 5:
        result = "*" + word + "*"
        print("유효한 입력 결과 :", result)
    else:
        result = "$" + word + "$"
        print("유효한 입력 결과 :", result)

