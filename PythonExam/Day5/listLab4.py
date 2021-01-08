import  random
listnum = []

for i in range(10):
    listnum.append(random.randint(1,50))
print(listnum)

for i in range(len(listnum)):
    if listnum[i] < 10:
        listnum[i] =100

print(listnum)
print(listnum[0])
print(listnum[9]) # listnum[-1], listnum[len(listnum)-1] 도 됨
print(listnum[1:6])
print(listnum[::-1]) # 몰랐던 것!, 전체를 역순으로 출력
print(listnum[:]) # 몰랐던 것, 전체출력방법
del listnum[4] # 인덱싱 방법 제거 맞음
print(listnum[:])
listnum[1:3] = [] # 2개 더 제거
print(listnum[:])

