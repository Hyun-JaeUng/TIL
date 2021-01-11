
x = [['B','C','A','A'], ['C','C','B','B'],['D','A','A','D']]
ans =[0,0,0,0]

# 조건에 따라 ans 리스트 값에 추가
for i in range(len(x)):
    for j in x[i]:
        if j == "A":
            ans[0] += 1
        elif j == "B":
            ans[1] += 1
        elif j == "C":
            ans[2] += 1
        elif j == "D":
            ans[3] += 1

# 출력
hp = ["A","B","C","D"]   # 자주 까먹는 것: 문자를 넣을 때 꼭 따옴표 붙이기
for i in range(0,4):
    print(hp[i], "는", ans[i], "개 입니다.")

#chr(65+i)도 활용 가능했음!



