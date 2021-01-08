listnum = [10,5,7,21,4,8,18]
min_num = 0

for i in range(len(listnum)):
    if i == 0:
        min_num = listnum[0]
    else:
        if min_num <= listnum[i]:
            pass
        else:
            min_num = listnum[i]

print("최솟값 :", min_num)

