ans = []
x = []

# 조건에 맞는 이차원 리스트 생성
for i in range(10,51,10):
    x.append(i)
ans.append(x)
x = []

for i in range(5,16,5):
    x.append(i)
ans.append(x)
x = []

for i in range(11,45,11):
    x.append(i)
ans.append(x)
x = []

for i in range(9,1,-1):
    x.append(i)
x.append(13)
ans.append(x)

# 행단위 합 구하기
for i in range(len(ans)):
    sum = 0
    for j in ans[i]:
        sum += j
    print(i+1, "행의 합은", sum, "입니다.")



