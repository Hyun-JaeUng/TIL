x =[]
for i in range(10,35,8):
    y =[]
    for j in range (i,i+7,2):
        y.append(j)
    x.append(y)
print(x)
print(x[0][0])
print(x[2][3])
print(len(x)) #행의 갯수
print(len(x[0])) #열의 갯수
print(x[2]) # 3행의 데이터

# 2열의 데이터
for i in range(len(x[0])):
    print(x[i][1], end=" ")
print() # 개행

# 왼쪽 대각선
for i in range(len(x[0])):
    print(x[i][i], end=" ")
print() # 개행

# 오른쪽 대각선
for i in range(len(x[0])):
    print(x[i][len(x[0])-(i+1)], end=" ")
